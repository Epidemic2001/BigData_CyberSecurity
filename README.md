# Del log a la alerta en milisegundos

`PROYECTO BIG DATA · CIBERSEGURIDAD`

> Big Data aplicado a la Ciberseguridad: por qué lo hacemos, con qué datos y con qué arquitectura.

Especificación de diseño de la infografía que presenta y justifica el inicio del proyecto.
Formato recomendado: vertical, 1080 × 3840 px (digital) o A3 vertical (impresión).

Alternativas con un tono más institucional:

- *Ciberseguridad a escala de datos* — El caso para una plataforma de detección en tiempo real.
- *Cuando la defensa se vuelve analítica* — Arquitectura de ingesta para detección de amenazas.

---

## Paleta y estilo visual

Oscuro tecnológico, sobrio y corporativo. Fondo profundo, tarjetas apenas elevadas, y solo tres colores de acento con significado fijo. Sin degradados decorativos ni fotos de "hackers con capucha".

**El color indica el origen del dato.** El lector debe poder seguir cada corriente de arriba a abajo sin leer.

| Rol | Color | Hex | Dónde se usa |
|---|---|---|---|
| Fondo | Azul noche | `#0B1220` | Lienzo completo |
| Superficie | Azul pizarra | `#131C2E` | Tarjetas y nodos |
| Borde / rejilla | Azul acero | `#24324A` | Contornos, líneas divisorias |
| Texto principal | Blanco frío | `#E6EDF7` | Encabezados y texto |
| Texto secundario | Gris azulado | `#8FA3BF` | Rótulos, notas |
| **Telemetría interna** | Cian | `#22D3EE` | Todo el flujo interno: Vector, Kafka, líneas de datos |
| **Inteligencia externa** | Ámbar | `#F5A623` | Feeds externos, Redis, IOCs |
| **Amenaza detectada** | Rojo coral | `#FF4D5E` | Solo la coincidencia y la alerta etiquetada |

El rojo aparece en un único punto de la pieza: donde el cian y el ámbar se encuentran en Flink. Esa escasez es lo que le da fuerza.

**Tipografía**

- Encabezados: **Space Grotesk** (Bold / Medium)
- Texto: **Inter** (Regular, 400)
- Rótulos técnicos y microdatos: **JetBrains Mono** (mayúsculas, tracking amplio)

**Iconografía:** trazo lineal de 2 px, esquinas redondeadas, monocromo en el color de su corriente. Un solo set para toda la pieza (Phosphor o Lucide funcionan bien).

**Líneas de flujo:** trazo de 3 px con puntos pequeños que sugieren movimiento. Continuas para el flujo interno (streaming), discontinuas para el externo (asíncrono, por lotes programados).

---

## Estructura general

```
┌──────────────────────────────────────────────┐
│  CABECERA                                    │
│  Del log a la alerta en milisegundos         │
├──────────────────────────────────────────────┤
│  01 · EL PORQUÉ                              │
│  Frase-tesis + tira "antes → hoy"            │
│  [ Volumen ]  [ Velocidad ]  [ Memoria ]     │
├──────────────────────────────────────────────┤
│  02 · FUENTES DE DATOS                       │
│  [ Telemetría interna ]  [ Intel. externa ]  │
│        cian │                  │ ámbar       │
├─────────────┼──────────────────┼─────────────┤
│  03 · ESTRATEGIA Y HERRAMIENTAS DE INGESTA   │
│             ▼                  │             │
│      ① Vector + VRL            │             │
│             ▼                  ▼             │
│      ② Apache Kafka        ③ Redis           │
│             ▼                  ▲             │
│      ④ Apache Flink ◀──────────┘             │
│             ▼ rojo                           │
│      Almacenamiento final                    │
├──────────────────────────────────────────────┤
│  CIERRE                                      │
│  Frase de remate · equipo · fecha            │
└──────────────────────────────────────────────┘
```

Las dos líneas de color nacen en las tarjetas del bloque 02 y bajan sin interrupción hasta el bloque 03. Esa continuidad es la que convierte tres secciones en una sola historia.

En la cabecera, una línea horizontal fina de puntos cian cruza de lado a lado y termina en un único punto rojo a la derecha. Resume toda la infografía en un gesto.

---

## 01 · El Porqué

**La ciberseguridad dejó de ser un problema de redes. Hoy es un desafío analítico masivo.**

Defender una organización significa evaluar gigabytes de telemetría sin pausa. Quien analiza más rápido, detecta antes.

Dos cápsulas unidas por una flecha:

- `ANTES` — Vigilar el perímetro de la red *(izquierda, apagada en gris)*
- `HOY` — Analizar datos a gran escala *(derecha, encendida en cian)*

Tres pilares, en tarjetas en fila:

| Pilar | Concepto | Descripción | Icono |
|---|---|---|---|
| **Volumen** | Gigabytes de telemetría | Cada firewall, endpoint y segmento de red genera eventos de forma continua. Evaluarlos todos ya no es monitoreo: es analítica masiva. | Capas apiladas / cilindros de datos |
| **Velocidad** | Detección en milisegundos | Las amenazas se identifican en tiempo real, mientras el evento todavía está en tránsito. | Cronómetro con rayo |
| **Memoria** | Retención a largo plazo | El historial completo queda disponible para el análisis forense: reconstruir qué pasó, cuándo y por dónde. | Lupa sobre línea de tiempo |

> Volumen, velocidad y memoria: por eso este es un proyecto de Big Data.

---

## 02 · Fuentes de Datos

**Dos corrientes de datos, un solo contexto**

El combustible del proyecto: lo que ocurre dentro de la organización y lo que el mundo ya sabe sobre las amenazas.

### Telemetría Interna — Lo que pasa dentro

`FLUJO CONTINUO · LOGS EN STREAMING`

Tarjeta izquierda, con borde y acentos en cian.

| Fuente | Descripción | Icono |
|---|---|---|
| **Firewalls** | Conexiones permitidas y bloqueadas. | Muro de ladrillos con llama o escudo |
| **Endpoints (EDR)** | Procesos, archivos y comportamiento en cada equipo. | Portátil con pulso |
| **Tráfico de red corporativa** | Quién se comunica con quién, cuánto y cuándo. | Nodos conectados |

### Inteligencia de Amenazas Externa — Lo que el mundo ya sabe

`FEEDS ASÍNCRONOS · CONSULTA PROGRAMADA DE APIS PÚBLICAS`

Tarjeta derecha, con borde y acentos en ámbar.

| Fuente | Descripción | Icono |
|---|---|---|
| **CISA KEV** | Catálogo de vulnerabilidades explotadas activamente. | Escudo con signo de exclamación |
| **Abuse.ch** | Ecosistema de repositorios de malware e IPs maliciosas. | Insecto (bug) dentro de un hexágono |
| **AlienVault OTX** | Red de inteligencia colaborativa global. | Globo con nodos |

### Convergencia

Las líneas cian y ámbar salen de cada tarjeta y bajan en paralelo hacia el bloque 03. Entre ambas, centrado:

> **Un evento interno es solo una línea de log. Cruzado con inteligencia externa, es una amenaza identificada.**

Un pequeño reloj junto a la línea ámbar refuerza que esa corriente llega por tandas programadas, no en continuo.

---

## 03 · Estrategia y Herramientas de Ingesta

**El motor: una arquitectura moderna y desacoplada**

Cuatro piezas, cuatro responsabilidades. Cada una hace una sola cosa, y la hace rápido.

### Diagrama de arquitectura

```
  TELEMETRÍA INTERNA                       INTELIGENCIA EXTERNA
  Firewalls · EDR · Red                    CISA KEV · Abuse.ch · AlienVault OTX
          │                                          ┆
          │ logs crudos (continuo)                   ┆ APIs públicas
          ▼                                          ┆ (carga programada)
  ┌────────────────────────┐                         ┆
  │ ①  VECTOR + VRL        │                         ┆
  │ Recolecta en el borde  │                         ┆
  │ Normaliza a OCSF       │                         ┆
  └───────────┬────────────┘                         ┆
              │ eventos OCSF                         ┆
              ▼                                      ▼
  ┌────────────────────────┐            ┌────────────────────────┐
  │ ②  APACHE KAFKA        │            │ ③  REDIS               │
  │ Bus de eventos         │            │ Caché de IOCs          │
  │ inmutable              │            │ en memoria · < 1 ms    │
  └───────────┬────────────┘            └───────────▲────────────┘
              │ flujo ordenado                      │
              ▼                                     │
  ┌────────────────────────┐   consulta asíncrona   │
  │ ④  APACHE FLINK        │◀───────────────────────┘
  │ Enriquece al vuelo     │    "¿coincide con un IOC?"
  │ Etiqueta alertas       │
  └───────────┬────────────┘
              │ alertas etiquetadas (rojo)
              ▼
  ┌────────────────────────┐
  │ ALMACENAMIENTO FINAL   │
  │ Alertas + retención    │
  │ forense a largo plazo  │
  └────────────────────────┘
```

- Columna izquierda en cian: el camino del evento interno, de arriba a abajo.
- Columna derecha en ámbar con línea discontinua: la inteligencia externa, que desemboca en Redis.
- El único trazo horizontal es la consulta Flink ↔ Redis. Es el momento clave: ahí se dibuja el punto rojo.
- A partir de Flink, la línea de salida cambia de cian a rojo: el evento ya es una alerta etiquetada.

### ① Vector + VRL (Vector Remap Language) — Captura y normaliza en el borde

Recolecta los logs crudos de forma ultrarrápida en el *edge* y los normaliza al instante con VRL hacia OCSF (Open Cybersecurity Schema Framework), el estándar universal de eventos de seguridad.

`EDGE · LOGS CRUDOS → OCSF`

*Icono:* embudo con rayo; a su lado, tres formas distintas (círculo, triángulo, cuadrado) que entran y salen convertidas en una misma forma.

### ② Apache Kafka — El bus de eventos inmutable

Retiene los datos de forma ordenada y tolerante a fallos. Actúa como amortiguador: absorbe los picos de tráfico que genera un ataque para que el resto del sistema siga trabajando a su ritmo.

`AMORTIGUADOR · ORDENADO · TOLERANTE A FALLOS`

*Icono:* cinta de registros apilados en horizontal (log de solo-añadir); encima, una onda con un pico alto que entra y sale aplanada.

### ③ Redis — La memoria de amenazas

Base de datos en memoria (clave-valor) con latencia sub-milisegundo. Mantiene cacheados los Indicadores de Compromiso (IOCs) externos, listos para consultarse al instante.

`EN MEMORIA · CLAVE-VALOR · < 1 ms`

*Icono:* chip de memoria con una llave; debajo, dos o tres pares `clave → valor` en tipografía mono.

### ④ Apache Flink — El cerebro en tiempo real

Motor de procesamiento de flujos. Consume los datos de Kafka, consulta Redis de forma asíncrona para buscar coincidencias de amenazas —enriquecimiento al vuelo— y etiqueta las alertas antes de enviarlas al almacenamiento final.

`STREAMING · ENRIQUECIMIENTO AL VUELO · ALERTAS ETIQUETADAS`

*Icono:* engranaje atravesado por una flecha de flujo; a la salida, una etiqueta (tag) roja colgando del evento.

### Almacenamiento final

Alertas listas para actuar y eventos conservados a largo plazo para el análisis forense.

*Icono:* cilindro de base de datos con un pequeño reloj.

Nodo sin numerar y de estilo más discreto. Cierra el círculo con el bloque 01: tiempo real y retención a largo plazo.

### ¿Por qué desacoplada?

Tres microbeneficios en una fila, bajo el diagrama:

| Beneficio | Icono |
|---|---|
| **Resiste.** Si una pieza se detiene, Kafka conserva los eventos. | Escudo |
| **Escala.** Cada capa crece por separado, según su propia carga. | Flechas de expansión |
| **Evoluciona.** Se añaden fuentes nuevas sin rediseñar el flujo. | Pieza de puzle |

---

## Cierre

**Capturar en el borde. Amortiguar en Kafka. Recordar en Redis. Decidir en Flink.**

Este es el punto de partida de nuestro proyecto de Big Data aplicado a la Ciberseguridad.

`[Nombre del equipo] · [Asignatura / organización] · [Fecha]`

Los cuatro iconos del bloque 03 van en fila, pequeños, unidos por la línea cian que termina en el punto rojo, igual que en la cabecera.

---

## Lista de verificación de contenido

Todo lo que debe aparecer en la pieza final:

- [ ] Ciberseguridad como desafío analítico masivo, ya no como problema de redes
- [ ] Gigabytes de telemetría
- [ ] Detección en tiempo real (milisegundos)
- [ ] Retención a largo plazo para análisis forense
- [ ] Telemetría interna: firewalls, endpoints (EDR), tráfico de red corporativa
- [ ] Inteligencia externa por feeds asíncronos y APIs públicas programadas
- [ ] CISA KEV — vulnerabilidades explotadas activamente
- [ ] Abuse.ch — repositorios de malware e IPs maliciosas
- [ ] AlienVault OTX — inteligencia colaborativa global
- [ ] Convergencia visible de ambas corrientes
- [ ] Vector + VRL (Vector Remap Language) en el borde
- [ ] OCSF (Open Cybersecurity Schema Framework)
- [ ] Apache Kafka — bus inmutable, amortiguador, tolerante a fallos, picos de ataque
- [ ] Redis — en memoria, clave-valor, sub-milisegundo, IOCs cacheados
- [ ] Apache Flink — consume Kafka, consulta asíncrona a Redis, enriquecimiento al vuelo, etiquetado, envío al almacenamiento final

---

## Notas para quien maquete

- **Jerarquía:** el diagrama del bloque 03 es la pieza central y debe ocupar cerca del 45 % de la altura. Los bloques 01 y 02 son el preámbulo que lo justifica.
- **Densidad:** ningún texto supera las tres líneas a ancho de tarjeta. Si no cabe, se recorta el texto, no se reduce la tipografía.
- **Versión horizontal (16:9) para diapositivas:** el mismo contenido se reordena con el bloque 01 a la izquierda, el 02 arriba a la derecha y el diagrama del 03 en horizontal ocupando la franja inferior, con Redis colocado sobre Flink.
- **Precisión técnica del cruce:** Abuse.ch y AlienVault OTX aportan indicadores observables (IPs, dominios, hashes) que se comparan directamente con los eventos. CISA KEV aporta identificadores CVE, que se cruzan con los eventos que reportan vulnerabilidades. Si se ilustran claves de ejemplo en Redis, conviene reflejarlo: `ioc:ip:…`, `ioc:hash:…`, `kev:CVE-…`.
- **Acceso a los feeds:** CISA KEV se publica como JSON abierto. Abuse.ch y AlienVault OTX son gratuitos pero piden una clave de API asociada a una cuenta; conviene confirmarlo antes de planificar la carga programada. No afecta al diseño.

---

## Implementación de la ingesta

Método concreto para ingerir cada fuente de datos, con la configuración y el código necesarios. La telemetría interna entra por Vector y termina en Kafka normalizada a OCSF; la inteligencia externa la descarga un cargador en Python y termina en Redis.

| Fuente | Herramienta de origen | Método de ingesta | Destino |
|---|---|---|---|
| **Firewalls** | UFW / iptables (Linux) | rsyslog reenvía por TCP → Vector `syslog` → VRL | Kafka `ocsf.firewall` |
| **Endpoints (EDR)** | osquery | Log de resultados JSON → Vector `file` → VRL | Kafka `ocsf.edr` |
| **Tráfico de red** | Zeek | `conn.log` en JSON → Vector `file` → VRL | Kafka `ocsf.network` |
| **CISA KEV** | JSON abierto | `GET` cada 6 h | Redis `kev:<CVE>` |
| **Abuse.ch** | ThreatFox, URLhaus, MalwareBazaar, Feodo Tracker | `GET`/`POST` cada hora (Feodo cada 15 min) | Redis `ioc:*` |
| **AlienVault OTX** | API de pulsos suscritos | `GET` incremental cada hora | Redis `ioc:*` |

Versiones usadas: Vector 0.61.0, Apache Kafka 4.1.0 (KRaft, sin ZooKeeper), Redis 7 y Python 3.13.

### Requisitos

- Docker con Docker Compose.
- Una clave de abuse.ch (`Auth-Key`), gratuita, desde <https://auth.abuse.ch/>. Sirve para ThreatFox, URLhaus y MalwareBazaar. Feodo Tracker no la necesita.
- Una clave de AlienVault OTX, gratuita, visible en la página *Settings* de tu cuenta en <https://otx.alienvault.com>.
- CISA KEV no necesita clave.

### Estructura de archivos

```
.
├── docker-compose.yml
├── .env                      # claves de API; no se sube al repositorio
├── vector/
│   ├── vector.yaml           # opciones globales
│   ├── firewall.yaml         # fuente + transformación + destino del firewall
│   ├── edr.yaml              # ídem para osquery
│   ├── network.yaml          # ídem para Zeek
│   └── tests.yaml            # pruebas unitarias de las transformaciones
├── loader/
│   ├── requirements.txt
│   └── ioc_loader.py         # cargador de inteligencia externa
└── logs/
    ├── osquery/              # osqueryd.results.log
    └── zeek/                 # conn.log
```

### 1. Infraestructura base

`docker-compose.yml` levanta Kafka, crea los tres topics, y arranca Redis, Vector y el cargador de IOCs:

```yaml
services:
  kafka:
    image: apache/kafka:4.1.0
    ports:
      - "29092:29092"
    environment:
      KAFKA_NODE_ID: 1
      KAFKA_PROCESS_ROLES: broker,controller
      KAFKA_LISTENERS: INTERNAL://:9092,EXTERNAL://:29092,CONTROLLER://:9093
      KAFKA_ADVERTISED_LISTENERS: INTERNAL://kafka:9092,EXTERNAL://localhost:29092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT,CONTROLLER:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL
      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@kafka:9093
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS: 0
      KAFKA_AUTO_CREATE_TOPICS_ENABLE: "false"
    volumes:
      - kafka-data:/var/lib/kafka/data
    healthcheck:
      test: ["CMD-SHELL", "/opt/kafka/bin/kafka-broker-api-versions.sh --bootstrap-server localhost:9092 > /dev/null 2>&1"]
      interval: 10s
      timeout: 10s
      retries: 12

  kafka-init:
    image: apache/kafka:4.1.0
    depends_on:
      kafka:
        condition: service_healthy
    entrypoint: ["/bin/sh", "-c"]
    command:
      - |
        for t in ocsf.firewall ocsf.edr ocsf.network; do
          /opt/kafka/bin/kafka-topics.sh --bootstrap-server kafka:9092 \
            --create --if-not-exists --topic $$t \
            --partitions 3 --replication-factor 1 \
            --config retention.ms=604800000
        done

  redis:
    image: redis:7-alpine
    command: ["redis-server", "--appendonly", "yes"]
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data

  vector:
    image: timberio/vector:0.61.0-alpine
    command: ["--config-dir", "/etc/vector"]
    depends_on:
      kafka-init:
        condition: service_completed_successfully
    ports:
      - "5514:5514/tcp"
    volumes:
      - ./vector:/etc/vector:ro
      - ./logs/osquery:/var/log/osquery:ro
      - ./logs/zeek:/var/log/zeek:ro
      - vector-data:/var/lib/vector

  ioc-loader:
    image: python:3.13-slim
    working_dir: /app
    depends_on:
      - redis
    environment:
      REDIS_URL: redis://redis:6379/0
      ABUSECH_AUTH_KEY: ${ABUSECH_AUTH_KEY:-}
      OTX_API_KEY: ${OTX_API_KEY:-}
    volumes:
      - ./loader:/app:ro
    command: ["sh", "-c", "pip install --no-cache-dir -r requirements.txt && python ioc_loader.py"]

volumes:
  kafka-data:
  redis-data:
  vector-data:
```

`.env`, junto al `docker-compose.yml`, con las dos claves. Hay que crearlo a mano: el `.gitignore` del repositorio lo excluye para que no se publiquen.

```
ABUSECH_AUTH_KEY=tu_clave_de_abuse_ch
OTX_API_KEY=tu_clave_de_otx
```

`vector/vector.yaml`:

```yaml
data_dir: /var/lib/vector
```

Arranque:

```bash
docker compose up -d
```

Kafka se anuncia como `kafka:9092` dentro de la red de Docker y como `localhost:29092` hacia fuera. Si Vector va a correr en otras máquinas (un agente por firewall, endpoint o sensor), cambia `EXTERNAL://localhost:29092` por la IP del servidor de Kafka y usa esa dirección en `bootstrap_servers`.

### 2. Telemetría interna

Las tres fuentes siguen el mismo patrón en Vector: una fuente (`sources`) que recoge el log crudo, una transformación `remap` con VRL que lo convierte a OCSF 1.3.0, y un destino (`sinks`) de Kafka. Las líneas que no son del tipo esperado se descartan con `abort`, y las que fallan al parsear, con `drop_on_error`.

#### 2.1 Firewalls: UFW / iptables por syslog

En el firewall, activa el registro y reenvía solo las líneas de UFW a Vector por TCP:

```bash
sudo ufw logging on
```

`/etc/rsyslog.d/60-vector.conf` (sustituye `IP_DE_VECTOR`; `@@` significa TCP):

```
:msg, contains, "[UFW " @@IP_DE_VECTOR:5514
```

```bash
sudo systemctl restart rsyslog
```

`vector/firewall.yaml`:

```yaml
sources:
  fw_syslog:
    type: syslog
    address: 0.0.0.0:5514
    mode: tcp

transforms:
  fw_ocsf:
    type: remap
    inputs: [fw_syslog]
    drop_on_error: true
    source: |
      msg = string!(.message)

      # Solo las líneas de UFW/iptables llevan SRC= y DST=
      if !contains(msg, "SRC=") || !contains(msg, "DST=") {
        abort
      }

      kv = parse_key_value!(msg, key_value_delimiter: "=", field_delimiter: " ")

      bloqueado = match(msg, r'BLOCK|DROP|REJECT|DENY')
      proto = downcase(string(kv.PROTO) ?? "")
      proto_num = if proto == "tcp" { 6 } else if proto == "udp" { 17 } else if proto == "icmp" { 1 } else { to_int(proto) ?? 0 }
      activity_id = if bloqueado { 5 } else { 6 }
      activity_name = if bloqueado { "Refuse" } else { "Traffic" }
      action_id = if bloqueado { 2 } else { 1 }
      action = if bloqueado { "Denied" } else { "Allowed" }
      # IN= y OUT= pueden venir vacíos, así que se extraen aparte con una regex
      ifaces = parse_regex(msg, r'IN=(?P<entrada>\S*) OUT=(?P<salida>\S*)') ?? {}
      entrada = string(ifaces.entrada) ?? ""
      salida = string(ifaces.salida) ?? ""
      direction_id = if entrada != "" && salida == "" { 1 } else if salida != "" && entrada == "" { 2 } else { 0 }

      . = {
        "category_uid": 4,
        "category_name": "Network Activity",
        "class_uid": 4001,
        "class_name": "Network Activity",
        "activity_id": activity_id,
        "activity_name": activity_name,
        "type_uid": 400100 + activity_id,
        "time": to_unix_timestamp(timestamp(.timestamp) ?? now(), unit: "milliseconds"),
        "severity_id": 1,
        "action_id": action_id,
        "action": action,
        "src_endpoint": { "ip": kv.SRC, "port": to_int(kv.SPT) ?? null, "interface_name": entrada },
        "dst_endpoint": { "ip": kv.DST, "port": to_int(kv.DPT) ?? null },
        "connection_info": { "protocol_num": proto_num, "protocol_name": proto, "direction_id": direction_id },
        "device": { "hostname": .host },
        "metadata": {
          "version": "1.3.0",
          "log_name": "firewall",
          "product": { "name": "UFW", "vendor_name": "Netfilter" }
        },
        "raw_data": msg
      }
      . = compact(.)

sinks:
  kafka_firewall:
    type: kafka
    inputs: [fw_ocsf]
    bootstrap_servers: kafka:9092
    topic: ocsf.firewall
    key_field: src_endpoint.ip
    compression: lz4
    encoding:
      codec: json
```

Cada evento sale como *Network Activity* (`class_uid` 4001): `Refuse` con `action_id` 2 si el paquete fue bloqueado, `Traffic` con `action_id` 1 si fue permitido. Para otro fabricante (FortiGate, pfSense) solo cambian los nombres de campo dentro del VRL; la fuente y el destino son los mismos.

#### 2.2 Endpoints (EDR): osquery

En cada endpoint, instala osquery y programa una consulta que lista los procesos con su hash SHA-256. `/etc/osquery/osquery.conf`:

```json
{
  "options": {
    "logger_plugin": "filesystem",
    "logger_path": "/var/log/osquery",
    "host_identifier": "hostname"
  },
  "schedule": {
    "edr_procesos": {
      "query": "SELECT p.pid, p.name, p.path, p.cmdline, p.parent, p.uid, u.username, h.sha256 FROM processes p LEFT JOIN users u ON p.uid = u.uid LEFT JOIN hash h ON p.path = h.path;",
      "interval": 60
    }
  }
}
```

```bash
sudo systemctl enable --now osqueryd
```

osquery escribe una línea JSON por cada proceso que aparece (`"action": "added"`) o desaparece (`"removed"`) en `/var/log/osquery/osqueryd.results.log`. El nombre de la consulta, `edr_procesos`, es el que filtra el VRL.

`vector/edr.yaml`:

```yaml
sources:
  edr_osquery:
    type: file
    include:
      - /var/log/osquery/osqueryd.results.log
    read_from: beginning

transforms:
  edr_ocsf:
    type: remap
    inputs: [edr_osquery]
    drop_on_error: true
    source: |
      e = object!(parse_json!(string!(.message)))

      # Solo la consulta programada de procesos
      if e.name != "edr_procesos" {
        abort
      }

      c = object!(e.columns)
      activity_id = if e.action == "removed" { 2 } else { 1 }
      activity_name = if activity_id == 2 { "Terminate" } else { "Launch" }
      sha256 = downcase(string(c.sha256) ?? "")
      hashes = if sha256 == "" { [] } else { [{ "algorithm_id": 3, "algorithm": "SHA-256", "value": sha256 }] }

      . = {
        "category_uid": 1,
        "category_name": "System Activity",
        "class_uid": 1007,
        "class_name": "Process Activity",
        "activity_id": activity_id,
        "activity_name": activity_name,
        "type_uid": 100700 + activity_id,
        "time": to_int!(e.unixTime) * 1000,
        "severity_id": 1,
        "device": { "hostname": e.hostIdentifier },
        "actor": { "user": { "uid": c.uid, "name": c.username } },
        "process": {
          "pid": to_int(c.pid) ?? null,
          "name": c.name,
          "cmd_line": c.cmdline,
          "file": { "path": c.path, "name": c.name, "hashes": hashes },
          "parent_process": { "pid": to_int(c.parent) ?? null }
        },
        "metadata": {
          "version": "1.3.0",
          "log_name": "edr",
          "product": { "name": "osquery", "vendor_name": "osquery" }
        }
      }
      . = compact(.)

sinks:
  kafka_edr:
    type: kafka
    inputs: [edr_ocsf]
    bootstrap_servers: kafka:9092
    topic: ocsf.edr
    key_field: device.hostname
    compression: lz4
    encoding:
      codec: json
```

Cada evento sale como *Process Activity* (`class_uid` 1007), `Launch` o `Terminate`, con el hash del ejecutable en `process.file.hashes`, listo para cruzarse con los IOCs de tipo hash.

#### 2.3 Tráfico de red: Zeek

En el sensor de red, activa la salida en JSON añadiendo esta línea a `local.zeek` (en `/opt/zeek/share/zeek/site/`):

```
@load policy/tuning/json-logs.zeek
```

```bash
sudo zeekctl deploy
```

Zeek escribe una línea por conexión en `/opt/zeek/logs/current/conn.log`. Monta esa carpeta en el contenedor de Vector en lugar de `./logs/zeek`.

`vector/network.yaml`:

```yaml
sources:
  net_zeek:
    type: file
    include:
      - /var/log/zeek/conn.log
    read_from: beginning

transforms:
  net_ocsf:
    type: remap
    inputs: [net_zeek]
    drop_on_error: true
    source: |
      e = object!(parse_json!(string!(.message)))

      origen = e."id.orig_h"
      destino = e."id.resp_h"
      if is_null(origen) || is_null(destino) {
        abort
      }

      proto = downcase(string(e.proto) ?? "")
      proto_num = if proto == "tcp" { 6 } else if proto == "udp" { 17 } else if proto == "icmp" { 1 } else { 0 }
      estado = string(e.conn_state) ?? ""
      activity_id = if estado == "REJ" { 5 } else if estado == "S0" { 4 } else if estado == "RSTO" || estado == "RSTR" { 3 } else { 6 }
      activity_name = if activity_id == 5 { "Refuse" } else if activity_id == 4 { "Fail" } else if activity_id == 3 { "Reset" } else { "Traffic" }

      . = {
        "category_uid": 4,
        "category_name": "Network Activity",
        "class_uid": 4001,
        "class_name": "Network Activity",
        "activity_id": activity_id,
        "activity_name": activity_name,
        "type_uid": 400100 + activity_id,
        "time": to_int(to_float!(e.ts) * 1000),
        "duration": to_int((to_float(e.duration) ?? 0.0) * 1000),
        "severity_id": 1,
        "src_endpoint": { "ip": origen, "port": e."id.orig_p" },
        "dst_endpoint": { "ip": destino, "port": e."id.resp_p" },
        "connection_info": { "uid": e.uid, "protocol_num": proto_num, "protocol_name": proto },
        "app_name": e.service,
        "traffic": {
          "bytes_out": e.orig_bytes,
          "bytes_in": e.resp_bytes,
          "packets_out": e.orig_pkts,
          "packets_in": e.resp_pkts
        },
        "metadata": {
          "version": "1.3.0",
          "log_name": "network",
          "product": { "name": "Zeek", "vendor_name": "Zeek" }
        }
      }
      . = compact(.)

sinks:
  kafka_network:
    type: kafka
    inputs: [net_ocsf]
    bootstrap_servers: kafka:9092
    topic: ocsf.network
    key_field: src_endpoint.ip
    compression: lz4
    encoding:
      codec: json
```

Cada conexión sale como *Network Activity* (`class_uid` 4001) con origen, destino, bytes y paquetes en cada sentido. El estado de Zeek decide la actividad: `REJ` → `Refuse`, `S0` → `Fail`, `RSTO`/`RSTR` → `Reset`, el resto → `Traffic`.

#### 2.4 Pruebas de las transformaciones

`vector/tests.yaml` comprueba cada transformación con una línea de ejemplo, sin necesidad de Kafka:

```yaml
tests:
  - name: firewall UFW bloqueado a OCSF
    inputs:
      - insert_at: fw_ocsf
        type: log
        log_fields:
          host: fw01
          message: "[UFW BLOCK] IN=eth0 OUT= MAC=00:16:3e:aa:bb:cc:00:16:3e:dd:ee:ff:08:00 SRC=203.0.113.5 DST=10.0.0.2 LEN=40 TOS=0x00 PREC=0x00 TTL=245 ID=54321 PROTO=TCP SPT=44321 DPT=22 WINDOW=1024 RES=0x00 SYN URGP=0"
    outputs:
      - extract_from: fw_ocsf
        conditions:
          - type: vrl
            source: |
              assert_eq!(.class_uid, 4001)
              assert_eq!(.type_uid, 400105)
              assert_eq!(.action_id, 2)
              assert_eq!(.src_endpoint.ip, "203.0.113.5")
              assert_eq!(.src_endpoint.port, 44321)
              assert_eq!(.dst_endpoint.port, 22)
              assert_eq!(.connection_info.protocol_num, 6)
              assert_eq!(.connection_info.direction_id, 1)
              assert_eq!(.device.hostname, "fw01")

  - name: firewall UFW permitido de salida a OCSF
    inputs:
      - insert_at: fw_ocsf
        type: log
        log_fields:
          host: fw01
          message: "[UFW ALLOW] IN= OUT=eth0 SRC=10.0.0.2 DST=198.51.100.7 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=1234 DF PROTO=UDP SPT=5353 DPT=53 LEN=40"
    outputs:
      - extract_from: fw_ocsf
        conditions:
          - type: vrl
            source: |
              assert_eq!(.type_uid, 400106)
              assert_eq!(.action_id, 1)
              assert_eq!(.connection_info.protocol_num, 17)
              assert_eq!(.connection_info.direction_id, 2)
              assert_eq!(.dst_endpoint.ip, "198.51.100.7")
              assert!(!exists(.src_endpoint.interface_name))

  - name: firewall descarta lineas que no son del cortafuegos
    inputs:
      - insert_at: fw_ocsf
        type: log
        log_fields:
          host: fw01
          message: "usb 1-1: new high-speed USB device number 2 using xhci_hcd"
    no_outputs_from:
      - fw_ocsf

  - name: EDR osquery proceso a OCSF
    inputs:
      - insert_at: edr_ocsf
        type: log
        log_fields:
          message: '{"name":"edr_procesos","hostIdentifier":"ws-01","calendarTime":"Wed Nov 11 10:15:02 2026 UTC","unixTime":1794392102,"epoch":0,"counter":3,"numerics":false,"columns":{"cmdline":"curl http://198.51.100.7/a.sh","name":"curl","parent":"2211","path":"/usr/bin/curl","pid":"4312","sha256":"E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855","uid":"1000","username":"ana"},"action":"added"}'
    outputs:
      - extract_from: edr_ocsf
        conditions:
          - type: vrl
            source: |
              assert_eq!(.class_uid, 1007)
              assert_eq!(.type_uid, 100701)
              assert_eq!(.time, 1794392102000)
              assert_eq!(.process.pid, 4312)
              assert_eq!(.process.parent_process.pid, 2211)
              assert_eq!(.process.file.hashes[0].value, "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
              assert_eq!(.device.hostname, "ws-01")

  - name: red Zeek conn a OCSF
    inputs:
      - insert_at: net_ocsf
        type: log
        log_fields:
          message: '{"ts":1794392102.123456,"uid":"CHhAvVGS1DHFjwGM9","id.orig_h":"10.0.0.15","id.orig_p":51234,"id.resp_h":"198.51.100.7","id.resp_p":443,"proto":"tcp","service":"ssl","duration":2.5,"orig_bytes":1200,"resp_bytes":5400,"conn_state":"SF","orig_pkts":12,"resp_pkts":10}'
    outputs:
      - extract_from: net_ocsf
        conditions:
          - type: vrl
            source: |
              assert_eq!(.class_uid, 4001)
              assert_eq!(.type_uid, 400106)
              assert_eq!(.time, 1794392102123)
              assert_eq!(.duration, 2500)
              assert_eq!(.src_endpoint.ip, "10.0.0.15")
              assert_eq!(.dst_endpoint.port, 443)
              assert_eq!(.traffic.bytes_in, 5400)
              assert_eq!(.connection_info.uid, "CHhAvVGS1DHFjwGM9")
```

```bash
docker compose run --rm --no-deps vector test /etc/vector/vector.yaml /etc/vector/firewall.yaml /etc/vector/edr.yaml /etc/vector/network.yaml /etc/vector/tests.yaml
```

#### 2.5 Comprobación de extremo a extremo

Envía una línea de firewall de prueba al puerto de syslog:

```bash
docker compose exec -T vector sh -c 'printf "%s\n" "<4>Nov 11 10:15:02 fw01 kernel: [UFW BLOCK] IN=eth0 OUT= MAC=00:16:3e:aa:bb:cc:00:16:3e:dd:ee:ff:08:00 SRC=203.0.113.5 DST=10.0.0.2 LEN=40 TOS=0x00 PREC=0x00 TTL=245 ID=54321 PROTO=TCP SPT=44321 DPT=22 WINDOW=1024 RES=0x00 SYN URGP=0" | nc -w 2 127.0.0.1 5514'
```

Y lee el topic (cambia el nombre para `ocsf.edr` y `ocsf.network`):

```bash
docker compose exec -T kafka /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic ocsf.firewall --from-beginning --timeout-ms 6000 --property print.key=true
```

La salida es la clave del mensaje (la IP de origen) seguida del evento OCSF. Aquí se omite el campo `raw_data`, que lleva la línea original:

```json
{"action":"Denied","action_id":2,"activity_id":5,"activity_name":"Refuse","category_name":"Network Activity","category_uid":4,"class_name":"Network Activity","class_uid":4001,"connection_info":{"direction_id":1,"protocol_name":"tcp","protocol_num":6},"device":{"hostname":"fw01"},"dst_endpoint":{"ip":"10.0.0.2","port":22},"metadata":{"log_name":"firewall","product":{"name":"UFW","vendor_name":"Netfilter"},"version":"1.3.0"},"severity_id":1,"src_endpoint":{"interface_name":"eth0","ip":"203.0.113.5","port":44321},"time":1794392102000,"type_uid":400105}
```

### 3. Inteligencia de amenazas externa

Un único proceso en Python consulta cada API con su propia frecuencia y escribe los indicadores en Redis.

| Fuente | Petición | Autenticación | Frecuencia |
|---|---|---|---|
| CISA KEV | `GET https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` | Ninguna | 6 h |
| Feodo Tracker | `GET https://feodotracker.abuse.ch/downloads/ipblocklist.json` | Ninguna | 15 min |
| ThreatFox | `POST https://threatfox-api.abuse.ch/api/v1/` con `{"query": "get_iocs", "days": 1}` | Cabecera `Auth-Key` | 1 h |
| URLhaus | `GET https://urlhaus-api.abuse.ch/v1/urls/recent/` | Cabecera `Auth-Key` | 1 h |
| MalwareBazaar | `POST https://mb-api.abuse.ch/api/v1/` con `query=get_recent&selector=time` | Cabecera `Auth-Key` | 1 h |
| AlienVault OTX | `GET https://otx.alienvault.com/api/v1/pulses/subscribed?modified_since=…&limit=50` | Cabecera `X-OTX-API-KEY` | 1 h |

**Modelo de claves en Redis.** Cada indicador es un hash cuyo campo es la fuente que lo reporta y cuyo valor es un JSON con el contexto. Así un mismo indicador puede venir de varias fuentes sin pisarse, y a Flink le basta un `HGETALL` para saber si hay coincidencia y de quién.

| Clave | Contenido | Caducidad |
|---|---|---|
| `ioc:ip:<ip>` | IPs de C2 y de distribución de malware | 30 días (Feodo: 2 días) |
| `ioc:domain:<dominio>` | Dominios y hostnames maliciosos | 30 días |
| `ioc:url:<url>` | URLs de distribución de malware | 30 días |
| `ioc:hash:<hash>` | Hashes MD5, SHA-1 y SHA-256 de muestras | 30 días |
| `kev:<CVE>` | Entrada del catálogo KEV | Sin caducidad |
| `meta:feed:<fuente>` | Última ejecución y número de elementos | Sin caducidad |

La caducidad se renueva cada vez que la fuente vuelve a reportar el indicador, de modo que los que dejan de aparecer se borran solos. Dominios y hashes se guardan en minúsculas. De URLhaus solo se guarda el host como IOC cuando es una IP, porque un dominio puede ser un servicio legítimo que aloja el fichero malicioso. En OTX la carga es incremental: la marca de tiempo de la última pasada se guarda en `meta:otx:modified_since`, y la primera vez se piden los últimos 7 días.

`loader/requirements.txt`:

```
requests>=2.32
redis>=5.0
```

`loader/ioc_loader.py`:

```python
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
```

El servicio `ioc-loader` del `docker-compose.yml` lo deja corriendo de forma continua. Para lanzar una pasada manual de todas las fuentes, o de una sola:

```bash
docker compose run --rm ioc-loader sh -c "pip install -q -r requirements.txt && python ioc_loader.py --once"
```

```bash
docker compose run --rm ioc-loader sh -c "pip install -q -r requirements.txt && python ioc_loader.py --once --only cisa_kev"
```

Comprobación en Redis:

```bash
docker compose exec -T redis redis-cli hgetall kev:CVE-2021-44228
```

```bash
docker compose exec -T redis redis-cli hgetall meta:feed:feodo
```

```bash
docker compose exec -T redis redis-cli --scan --pattern "ioc:ip:*"
```

### 4. Qué campo se cruza con qué clave

| Campo del evento OCSF | Topic | Clave de Redis |
|---|---|---|
| `src_endpoint.ip`, `dst_endpoint.ip` | `ocsf.firewall`, `ocsf.network` | `ioc:ip:<ip>` |
| `process.file.hashes[].value` | `ocsf.edr` | `ioc:hash:<hash>` |

`ioc:domain`, `ioc:url` y `kev` quedan cargados pero ninguna de las tres fuentes internas actuales trae dominios, URLs ni CVEs. Se aprovecharán al añadir los logs `dns.log` y `http.log` de Zeek y un escáner de vulnerabilidades.

### Estado de las pruebas

Comprobado el 11 de noviembre de 2026 con Docker:

- Las cinco pruebas unitarias de Vector pasan y `vector validate` da la configuración por válida.
- Con Kafka, Redis y Vector levantados, una línea de cada fuente interna llegó a su topic ya convertida a OCSF.
- El cargador descargó CISA KEV (1.779 vulnerabilidades) y Feodo Tracker en vivo y los escribió en Redis.

No comprobado:

- ThreatFox, URLhaus, MalwareBazaar y OTX contra sus APIs reales, por no disponer de claves. Se probaron con respuestas simuladas construidas según el formato que documenta cada API.
- UFW, osquery y Zeek no se instalaron: las líneas de prueba siguen el formato que produce cada herramienta, y su configuración (rsyslog, `osquery.conf`, `local.zeek`) está sin ejecutar.
