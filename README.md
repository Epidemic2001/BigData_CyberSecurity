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

La telemetría interna entra por Vector y termina en Kafka normalizada a OCSF 1.3.0. La inteligencia externa la descarga un cargador en Python y termina en Redis. El código está en las carpetas del repositorio; aquí se explica qué hace cada parte.

| Ruta | Contenido |
|---|---|
| [`docker-compose.yml`](docker-compose.yml) | Kafka 4.1.0 (KRaft), creación de los topics, Redis 7, Vector 0.61.0 y el cargador de IOCs |
| [`vector/`](vector/) | Un archivo por fuente interna (recogida, conversión a OCSF y envío a Kafka) y sus pruebas |
| [`loader/`](loader/) | Cargador de inteligencia externa en Python |
| [`config/`](config/) | Configuración que se instala en cada origen: rsyslog, osquery y Zeek |
| [`logs/`](logs/) | Carpetas que Vector lee en el laboratorio |
| [`.env.example`](.env.example) | Plantilla para las claves de API |

### Telemetría interna

Las tres fuentes siguen el mismo proceso: Vector recoge el log crudo, lo convierte a OCSF con VRL y lo publica en su topic de Kafka. Las líneas que no son del tipo esperado o no se pueden interpretar se descartan.

**Firewalls (UFW / iptables)** — [`vector/firewall.yaml`](vector/firewall.yaml), [`config/rsyslog/60-vector.conf`](config/rsyslog/60-vector.conf)

- rsyslog reenvía a Vector, por TCP al puerto 5514, solo las líneas de UFW.
- Vector extrae IP y puerto de origen y destino, protocolo, interfaz y sentido de la conexión.
- Cada línea sale como *Network Activity* (4001): `Refuse` si el paquete fue bloqueado, `Traffic` si fue permitido.
- Se publica en `ocsf.firewall`, con la IP de origen como clave del mensaje.

**Endpoints (osquery)** — [`vector/edr.yaml`](vector/edr.yaml), [`config/osquery/osquery.conf`](config/osquery/osquery.conf)

- Cada 60 segundos osquery lista los procesos en ejecución con su usuario y el SHA-256 del ejecutable.
- Escribe una línea JSON por cada proceso que aparece o desaparece, y Vector lee ese archivo de resultados.
- Cada línea sale como *Process Activity* (1007): `Launch` o `Terminate`, con el hash en `process.file.hashes`.
- Se publica en `ocsf.edr`, con el nombre del equipo como clave del mensaje.

**Tráfico de red (Zeek)** — [`vector/network.yaml`](vector/network.yaml), [`config/zeek/local.zeek`](config/zeek/local.zeek)

- Zeek escribe `conn.log` en JSON, una línea por conexión, y Vector lee ese archivo.
- Cada conexión sale como *Network Activity* (4001) con origen, destino, duración, y bytes y paquetes en cada sentido.
- El estado de Zeek decide la actividad: `REJ` es `Refuse`, `S0` es `Fail`, `RSTO` y `RSTR` son `Reset`, y el resto `Traffic`.
- Se publica en `ocsf.network`, con la IP de origen como clave del mensaje.

Las transformaciones se comprueban con [`vector/tests.yaml`](vector/tests.yaml): cinco pruebas con líneas de ejemplo de cada fuente, que no necesitan Kafka.

### Inteligencia de amenazas externa

[`loader/ioc_loader.py`](loader/ioc_loader.py) consulta cada API con su propia frecuencia y escribe los indicadores en Redis.

| Fuente | Qué se descarga | Clave de API | Frecuencia | Se guarda como |
|---|---|---|---|---|
| CISA KEV | Catálogo completo de vulnerabilidades explotadas | No | 6 h | `kev:<CVE>` |
| Feodo Tracker (abuse.ch) | IPs de servidores C2 de botnets | No | 15 min | `ioc:ip` |
| ThreatFox (abuse.ch) | IOCs de las últimas 24 h: IPs, dominios, URLs y hashes | Sí | 1 h | `ioc:ip`, `ioc:domain`, `ioc:url`, `ioc:hash` |
| URLhaus (abuse.ch) | URLs de distribución de malware de los últimos 3 días | Sí | 1 h | `ioc:url`, `ioc:ip` |
| MalwareBazaar (abuse.ch) | SHA-256 de las muestras de los últimos 60 min | Sí | 1 h | `ioc:hash` |
| AlienVault OTX | Indicadores de los pulsos suscritos, modificados desde la última pasada | Sí | 1 h | `ioc:ip`, `ioc:domain`, `ioc:url`, `ioc:hash` |

Cómo se guardan en Redis:

- Cada indicador es un hash con la forma `ioc:<tipo>:<valor>`. El campo es la fuente que lo reporta y el valor, un JSON con el contexto (malware, tipo de amenaza, fecha, referencia). Así un mismo indicador puede venir de varias fuentes sin pisarse.
- Los indicadores caducan a los 30 días (2 días los de Feodo). La caducidad se renueva cada vez que la fuente lo vuelve a reportar, de modo que los que dejan de aparecer se borran solos.
- El catálogo KEV no caduca.
- De URLhaus, el host solo se guarda como IOC cuando es una IP: un dominio puede ser un servicio legítimo que aloja el fichero malicioso.
- En OTX se omiten los indicadores inactivos. La primera pasada pide los últimos 7 días.
- Si falta una clave de API, esa fuente se omite y las demás siguen cargándose.

### Cruce entre eventos e indicadores

| Campo del evento OCSF | Topic | Clave de Redis |
|---|---|---|
| `src_endpoint.ip`, `dst_endpoint.ip` | `ocsf.firewall`, `ocsf.network` | `ioc:ip:<ip>` |
| `process.file.hashes[].value` | `ocsf.edr` | `ioc:hash:<hash>` |

Los dominios, las URLs y el catálogo KEV quedan cargados, pero ninguna de las tres fuentes internas actuales trae esos datos. Se aprovecharán al añadir los logs `dns.log` y `http.log` de Zeek y un escáner de vulnerabilidades.

### Puesta en marcha

1. Copiar `.env.example` como `.env` y rellenar las dos claves. La de abuse.ch se obtiene en <https://auth.abuse.ch/> y la de OTX en la página *Settings* de la cuenta. Ambas son gratuitas.
2. Levantar el entorno con `docker compose up -d`.
3. En cada origen, instalar la configuración de [`config/`](config/). Los pasos están en los comentarios de cada archivo; `osquery.conf` se copia a `/etc/osquery/` y después se arranca el servicio `osqueryd`.

Kafka se anuncia como `kafka:9092` dentro de la red de Docker y como `localhost:29092` hacia fuera. Si Vector corre en otras máquinas, hay que cambiar esa dirección por la IP del servidor de Kafka en `docker-compose.yml` y en los archivos de `vector/`.

### Estado de las pruebas

Comprobado el 11 de noviembre de 2026 con Docker:

- Las cinco pruebas unitarias de Vector pasan.
- Una línea de cada fuente interna llegó a su topic de Kafka ya convertida a OCSF.
- El cargador descargó CISA KEV (1.779 vulnerabilidades) y Feodo Tracker en vivo y los escribió en Redis.

No comprobado:

- ThreatFox, URLhaus, MalwareBazaar y OTX contra sus APIs reales, por no disponer de claves. Se probaron con respuestas simuladas según el formato que documenta cada API.
- UFW, osquery y Zeek no se instalaron, así que los archivos de `config/` están sin ejecutar. Las pruebas usan líneas de ejemplo con el formato de cada herramienta.
