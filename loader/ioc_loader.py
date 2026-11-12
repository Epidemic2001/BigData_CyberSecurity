"""Carga programada de inteligencia de amenazas externa en Redis.

Fuentes: CISA KEV, abuse.ch (ThreatFox, URLhaus, Feodo Tracker, MalwareBazaar)
y AlienVault OTX.

Modelo de claves en Redis:
  kev:<CVE>            hash con los datos del catálogo KEV (sin caducidad)
  ioc:ip:<ip>          hash  campo = fuente, valor = JSON con el contexto
  ioc:domain:<dominio> hash  campo = fuente, valor = JSON con el contexto
  ioc:url:<url>        hash  campo = fuente, valor = JSON con el contexto
  ioc:hash:<hash>      hash  campo = fuente, valor = JSON con el contexto
"""

import argparse
import ipaddress
import json
import logging
import os
import time
from datetime import datetime, timedelta, timezone

import redis
import requests

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
ABUSECH_AUTH_KEY = os.getenv("ABUSECH_AUTH_KEY", "")
OTX_API_KEY = os.getenv("OTX_API_KEY", "")

IOC_TTL = 30 * 24 * 3600      # los IOCs caducan a los 30 días si no se vuelven a ver
FEODO_TTL = 2 * 24 * 3600     # la lista de Feodo se recarga entera en cada pasada
TIMEOUT = 60

log = logging.getLogger("ioc_loader")
r = redis.Redis.from_url(REDIS_URL, decode_responses=True)
http = requests.Session()
http.headers.update({"User-Agent": "ioc-loader/1.0"})


def guardar(pipe, tipo, valor, fuente, contexto, ttl=IOC_TTL):
    """Añade un IOC al pipeline. Devuelve 1 si se guardó y 0 si se descartó."""
    valor = (valor or "").strip()
    if tipo != "url":
        valor = valor.lower()
    if not valor:
        return 0
    clave = f"ioc:{tipo}:{valor}"
    contexto = {k: v for k, v in contexto.items() if v not in (None, "", [])}
    pipe.hset(clave, fuente, json.dumps(contexto, ensure_ascii=False))
    pipe.expire(clave, ttl)
    return 1


def es_ip(valor):
    try:
        ipaddress.ip_address(valor)
        return True
    except ValueError:
        return False


# --------------------------------------------------------------------------
# CISA KEV: JSON abierto, sin clave
# --------------------------------------------------------------------------
KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"


def cargar_cisa_kev():
    resp = http.get(KEV_URL, timeout=TIMEOUT)
    resp.raise_for_status()
    catalogo = resp.json()

    pipe = r.pipeline(transaction=False)
    for v in catalogo["vulnerabilities"]:
        pipe.hset(f"kev:{v['cveID']}", mapping={
            "vendor": v.get("vendorProject", ""),
            "product": v.get("product", ""),
            "name": v.get("vulnerabilityName", ""),
            "date_added": v.get("dateAdded", ""),
            "due_date": v.get("dueDate", ""),
            "ransomware": v.get("knownRansomwareCampaignUse", ""),
        })
    pipe.set("meta:kev:catalog_version", catalogo.get("catalogVersion", ""))
    pipe.execute()
    return len(catalogo["vulnerabilities"])


# --------------------------------------------------------------------------
# abuse.ch: todas las APIs piden la cabecera Auth-Key salvo Feodo Tracker
# --------------------------------------------------------------------------
def cargar_threatfox():
    resp = http.post(
        "https://threatfox-api.abuse.ch/api/v1/",
        headers={"Auth-Key": ABUSECH_AUTH_KEY},
        json={"query": "get_iocs", "days": 1},
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    cuerpo = resp.json()
    if cuerpo.get("query_status") != "ok":
        log.warning("threatfox: query_status=%s", cuerpo.get("query_status"))
        return 0

    total = 0
    pipe = r.pipeline(transaction=False)
    for i in cuerpo["data"]:
        contexto = {
            "threat": i.get("threat_type"),
            "malware": i.get("malware_printable"),
            "confidence": i.get("confidence_level"),
            "first_seen": i.get("first_seen"),
            "tags": i.get("tags"),
            "ref": f"https://threatfox.abuse.ch/ioc/{i.get('id')}/",
        }
        tipo, valor = i.get("ioc_type", ""), i.get("ioc", "")
        if tipo == "ip:port":
            ip, _, puerto = valor.rpartition(":")
            contexto["port"] = puerto
            total += guardar(pipe, "ip", ip, "threatfox", contexto)
        elif tipo == "domain":
            total += guardar(pipe, "domain", valor, "threatfox", contexto)
        elif tipo == "url":
            total += guardar(pipe, "url", valor, "threatfox", contexto)
        elif tipo.endswith("_hash"):
            total += guardar(pipe, "hash", valor, "threatfox", contexto)
    pipe.execute()
    return total


def cargar_urlhaus():
    resp = http.get(
        "https://urlhaus-api.abuse.ch/v1/urls/recent/",
        headers={"Auth-Key": ABUSECH_AUTH_KEY},
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    cuerpo = resp.json()
    if cuerpo.get("query_status") != "ok":
        log.warning("urlhaus: query_status=%s", cuerpo.get("query_status"))
        return 0

    total = 0
    pipe = r.pipeline(transaction=False)
    for u in cuerpo["urls"]:
        contexto = {
            "threat": u.get("threat"),
            "status": u.get("url_status"),
            "host": u.get("host"),
            "first_seen": u.get("date_added"),
            "tags": u.get("tags"),
            "ref": u.get("urlhaus_reference"),
        }
        total += guardar(pipe, "url", u.get("url"), "urlhaus", contexto)
        # El host solo se guarda si es una IP: un dominio puede ser un servicio
        # legítimo (CDN, repositorio de código) que aloja el fichero malicioso.
        if es_ip(u.get("host") or ""):
            total += guardar(pipe, "ip", u["host"], "urlhaus", contexto)
    pipe.execute()
    return total


def cargar_feodo():
    resp = http.get("https://feodotracker.abuse.ch/downloads/ipblocklist.json", timeout=TIMEOUT)
    resp.raise_for_status()

    total = 0
    pipe = r.pipeline(transaction=False)
    for c2 in resp.json():
        contexto = {
            "threat": "botnet_cc",
            "malware": c2.get("malware"),
            "port": c2.get("port"),
            "status": c2.get("status"),
            "first_seen": c2.get("first_seen"),
            "last_online": c2.get("last_online"),
        }
        total += guardar(pipe, "ip", c2.get("ip_address"), "feodo", contexto, ttl=FEODO_TTL)
    pipe.execute()
    return total


def cargar_malwarebazaar():
    resp = http.post(
        "https://mb-api.abuse.ch/api/v1/",
        headers={"Auth-Key": ABUSECH_AUTH_KEY},
        data={"query": "get_recent", "selector": "time"},   # últimos 60 minutos
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    cuerpo = resp.json()
    if cuerpo.get("query_status") != "ok":
        log.info("malwarebazaar: query_status=%s", cuerpo.get("query_status"))
        return 0

    total = 0
    pipe = r.pipeline(transaction=False)
    for m in cuerpo["data"]:
        contexto = {
            "threat": "payload",
            "malware": m.get("signature"),
            "file_type": m.get("file_type"),
            "first_seen": m.get("first_seen"),
            "tags": m.get("tags"),
        }
        total += guardar(pipe, "hash", m.get("sha256_hash"), "malwarebazaar", contexto)
    pipe.execute()
    return total


# --------------------------------------------------------------------------
# AlienVault OTX: pulsos suscritos, carga incremental con modified_since
# --------------------------------------------------------------------------
OTX_URL = "https://otx.alienvault.com/api/v1/pulses/subscribed"
OTX_TIPOS = {
    "IPv4": "ip",
    "IPv6": "ip",
    "domain": "domain",
    "hostname": "domain",
    "URL": "url",
    "FileHash-MD5": "hash",
    "FileHash-SHA1": "hash",
    "FileHash-SHA256": "hash",
}


def cargar_otx():
    ahora = datetime.now(timezone.utc)
    desde = r.get("meta:otx:modified_since") or (ahora - timedelta(days=7)).isoformat(timespec="seconds")

    total = 0
    url = OTX_URL
    params = {"limit": 50, "modified_since": desde}
    while url:
        resp = http.get(url, params=params, headers={"X-OTX-API-KEY": OTX_API_KEY}, timeout=TIMEOUT)
        resp.raise_for_status()
        cuerpo = resp.json()

        pipe = r.pipeline(transaction=False)
        for pulso in cuerpo.get("results", []):
            for ind in pulso.get("indicators", []):
                tipo = OTX_TIPOS.get(ind.get("type"))
                if tipo is None or ind.get("is_active") in (False, 0):
                    continue
                contexto = {
                    "pulse": pulso.get("name"),
                    "adversary": pulso.get("adversary"),
                    "tags": pulso.get("tags"),
                    "first_seen": ind.get("created"),
                    "ref": f"https://otx.alienvault.com/pulse/{pulso.get('id')}",
                }
                total += guardar(pipe, tipo, ind.get("indicator"), "otx", contexto)
        pipe.execute()

        url = cuerpo.get("next")   # la URL siguiente ya trae todos los parámetros
        params = None

    r.set("meta:otx:modified_since", ahora.isoformat(timespec="seconds"))
    return total


# --------------------------------------------------------------------------
# Planificador: (nombre, función, intervalo en segundos, variable con la clave)
# --------------------------------------------------------------------------
FEEDS = [
    ("cisa_kev", cargar_cisa_kev, 6 * 3600, None),
    ("feodo", cargar_feodo, 15 * 60, None),
    ("threatfox", cargar_threatfox, 3600, "ABUSECH_AUTH_KEY"),
    ("urlhaus", cargar_urlhaus, 3600, "ABUSECH_AUTH_KEY"),
    ("malwarebazaar", cargar_malwarebazaar, 3600, "ABUSECH_AUTH_KEY"),
    ("otx", cargar_otx, 3600, "OTX_API_KEY"),
]


def ejecutar(nombre, funcion, variable):
    if variable and not os.getenv(variable):
        log.warning("%s: omitido, falta la variable %s", nombre, variable)
        return
    try:
        inicio = time.monotonic()
        total = funcion()
        r.hset(f"meta:feed:{nombre}", mapping={
            "last_run": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "items": total,
        })
        log.info("%s: %d elementos en %.1f s", nombre, total, time.monotonic() - inicio)
    except Exception:
        log.exception("%s: fallo en la carga", nombre)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--once", action="store_true", help="ejecuta cada fuente una vez y termina")
    parser.add_argument("--only", help="ejecuta solo la fuente indicada (por ejemplo cisa_kev)")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    feeds = [f for f in FEEDS if not args.only or f[0] == args.only]
    proxima = {nombre: 0.0 for nombre, *_ in feeds}
    while True:
        for nombre, funcion, intervalo, variable in feeds:
            if time.monotonic() >= proxima[nombre]:
                ejecutar(nombre, funcion, variable)
                proxima[nombre] = time.monotonic() + intervalo
        if args.once:
            break
        time.sleep(30)


if __name__ == "__main__":
    main()
