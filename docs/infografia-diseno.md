# Infografía — Especificación de diseño

**Proyecto:** Big Data aplicado a la Ciberseguridad
**Uso:** presentar y justificar el inicio del proyecto
**Formato recomendado:** vertical, 1080 × 3840 px (digital) o A3 vertical (impresión)

---

## 1. Título

**Título principal**

> # Del log a la alerta en milisegundos

**Subtítulo**

> Big Data aplicado a la Ciberseguridad: por qué lo hacemos, con qué datos y con qué arquitectura.

**Alternativas** (si se busca un tono más institucional):

- *Ciberseguridad a escala de datos* — El caso para una plataforma de detección en tiempo real.
- *Cuando la defensa se vuelve analítica* — Arquitectura de ingesta para detección de amenazas.

---

## 2. Paleta y estilo visual

**Estilo:** oscuro tecnológico, sobrio y corporativo. Fondo profundo, tarjetas apenas elevadas, y solo tres colores de acento con significado fijo. Sin degradados decorativos ni fotos de "hackers con capucha".

**Regla central: el color indica el origen del dato.** El lector debe poder seguir cada corriente de arriba a abajo sin leer.

| Rol | Color | Hex | Dónde se usa |
|---|---|---|---|
| Fondo | Azul noche | `#0B1220` | Lienzo completo |
| Superficie | Azul pizarra | `#131C2E` | Tarjetas y nodos |
| Borde / rejilla | Azul acero | `#24324A` | Contornos, líneas divisorias |
| Texto principal | Blanco frío | `#E6EDF7` | Títulos y cuerpo |
| Texto secundario | Gris azulado | `#8FA3BF` | Etiquetas, notas |
| **Telemetría interna** | Cian | `#22D3EE` | Todo el flujo interno: Vector, Kafka, líneas de datos |
| **Inteligencia externa** | Ámbar | `#F5A623` | Feeds externos, Redis, IOCs |
| **Amenaza detectada** | Rojo coral | `#FF4D5E` | Solo la coincidencia y la alerta etiquetada |

El rojo aparece en un único punto de la pieza: donde el cian y el ámbar se encuentran en Flink. Esa escasez es lo que le da fuerza.

**Tipografía**

- Títulos: **Space Grotesk** (Bold / Medium)
- Cuerpo: **Inter** (Regular, 400)
- Etiquetas técnicas y microdatos: **JetBrains Mono** (mayúsculas, tracking amplio)

**Iconografía:** trazo lineal de 2 px, esquinas redondeadas, monocromo en el color de su corriente. Un solo set para toda la pieza (Phosphor o Lucide funcionan bien).

**Líneas de flujo:** trazo de 3 px con puntos pequeños que sugieren movimiento. Continuas para el flujo interno (streaming), discontinuas para el externo (asíncrono, por lotes programados).

---

## 3. Estructura general (wireframe de página)

```
┌──────────────────────────────────────────────┐
│  CABECERA                                    │
│  Título · subtítulo · logo del equipo        │
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

---

## 4. Desglose bloque por bloque

### Cabecera

| Elemento | Texto exacto |
|---|---|
| Etiqueta superior | `PROYECTO BIG DATA · CIBERSEGURIDAD` |
| Título | **Del log a la alerta en milisegundos** |
| Subtítulo | Big Data aplicado a la Ciberseguridad: por qué lo hacemos, con qué datos y con qué arquitectura. |

**Visual:** una línea horizontal fina de puntos cian que cruza la cabecera y termina en un único punto rojo a la derecha. Resume toda la infografía en un gesto.

---

### Bloque 01 — El Porqué

| Elemento | Texto exacto |
|---|---|
| Etiqueta | `01 · EL PORQUÉ` |
| Titular | **La ciberseguridad dejó de ser un problema de redes. Hoy es un desafío analítico masivo.** |
| Entradilla | Defender una organización significa evaluar gigabytes de telemetría sin pausa. Quien analiza más rápido, detecta antes. |

**Tira "antes → hoy"** (dos cápsulas unidas por una flecha):

- Cápsula izquierda, apagada en gris: `ANTES` — Vigilar el perímetro de la red
- Cápsula derecha, encendida en cian: `HOY` — Analizar datos a gran escala

**Tres pilares** (tarjetas en fila):

| Pilar | Cifra-concepto | Texto exacto | Icono |
|---|---|---|---|
| **Volumen** | Gigabytes de telemetría | Cada firewall, endpoint y segmento de red genera eventos de forma continua. Evaluarlos todos ya no es monitoreo: es analítica masiva. | Capas apiladas / cilindros de datos |
| **Velocidad** | Detección en milisegundos | Las amenazas se identifican en tiempo real, mientras el evento todavía está en tránsito. | Cronómetro con rayo |
| **Memoria** | Retención a largo plazo | El historial completo queda disponible para el análisis forense: reconstruir qué pasó, cuándo y por dónde. | Lupa sobre línea de tiempo |

**Frase de cierre del bloque:**

> Volumen, velocidad y memoria: por eso este es un proyecto de Big Data.

---

### Bloque 02 — Fuentes de Datos

| Elemento | Texto exacto |
|---|---|
| Etiqueta | `02 · FUENTES DE DATOS` |
| Titular | **Dos corrientes de datos, un solo contexto** |
| Entradilla | El combustible del proyecto: lo que ocurre dentro de la organización y lo que el mundo ya sabe sobre las amenazas. |

**Tarjeta izquierda — borde y acentos en cian**

| Elemento | Texto exacto |
|---|---|
| Título | **Telemetría Interna** |
| Bajada | Lo que pasa dentro |
| Etiqueta técnica | `FLUJO CONTINUO · LOGS EN STREAMING` |

| Fuente | Texto exacto | Icono |
|---|---|---|
| **Firewalls** | Conexiones permitidas y bloqueadas. | Muro de ladrillos con llama o escudo |
| **Endpoints (EDR)** | Procesos, archivos y comportamiento en cada equipo. | Portátil con pulso |
| **Tráfico de red corporativa** | Quién se comunica con quién, cuánto y cuándo. | Nodos conectados |

**Tarjeta derecha — borde y acentos en ámbar**

| Elemento | Texto exacto |
|---|---|
| Título | **Inteligencia de Amenazas Externa** |
| Bajada | Lo que el mundo ya sabe |
| Etiqueta técnica | `FEEDS ASÍNCRONOS · CONSULTA PROGRAMADA DE APIS PÚBLICAS` |

| Fuente | Texto exacto | Icono |
|---|---|---|
| **CISA KEV** | Catálogo de vulnerabilidades explotadas activamente. | Escudo con signo de exclamación |
| **Abuse.ch** | Ecosistema de repositorios de malware e IPs maliciosas. | Insecto (bug) dentro de un hexágono |
| **AlienVault OTX** | Red de inteligencia colaborativa global. | Globo con nodos |

**Convergencia** (franja bajo las dos tarjetas): las líneas cian y ámbar salen de cada tarjeta y bajan en paralelo hacia el bloque 03. Entre ambas, centrado:

> **Un evento interno es solo una línea de log. Cruzado con inteligencia externa, es una amenaza identificada.**

Un pequeño reloj junto a la línea ámbar refuerza que esa corriente llega por tandas programadas, no en continuo.

---

### Bloque 03 — Estrategia y Herramientas de Ingesta

| Elemento | Texto exacto |
|---|---|
| Etiqueta | `03 · ESTRATEGIA Y HERRAMIENTAS DE INGESTA` |
| Titular | **El motor: una arquitectura moderna y desacoplada** |
| Entradilla | Cuatro piezas, cuatro responsabilidades. Cada una hace una sola cosa, y la hace rápido. |

#### Diagrama de arquitectura (wireframe)

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

**Lectura del diagrama**

- Columna izquierda en cian: el camino del evento interno, de arriba a abajo.
- Columna derecha en ámbar con línea discontinua: la inteligencia externa, que desemboca en Redis.
- El único trazo horizontal es la consulta Flink ↔ Redis. Es el momento clave: ahí se dibuja el punto rojo.
- A partir de Flink, la línea de salida cambia de cian a rojo: el evento ya es una alerta etiquetada.

#### Copy de cada paso

**① Vector + VRL (Vector Remap Language)**

| Elemento | Texto exacto |
|---|---|
| Rol | **Captura y normaliza en el borde** |
| Cuerpo | Recolecta los logs crudos de forma ultrarrápida en el *edge* y los normaliza al instante con VRL hacia OCSF (Open Cybersecurity Schema Framework), el estándar universal de eventos de seguridad. |
| Etiqueta técnica | `EDGE · LOGS CRUDOS → OCSF` |
| Icono | Embudo con rayo; a su lado, tres formas distintas (círculo, triángulo, cuadrado) que entran y salen convertidas en una misma forma |

**② Apache Kafka**

| Elemento | Texto exacto |
|---|---|
| Rol | **El bus de eventos inmutable** |
| Cuerpo | Retiene los datos de forma ordenada y tolerante a fallos. Actúa como amortiguador: absorbe los picos de tráfico que genera un ataque para que el resto del sistema siga trabajando a su ritmo. |
| Etiqueta técnica | `AMORTIGUADOR · ORDENADO · TOLERANTE A FALLOS` |
| Icono | Cinta de registros apilados en horizontal (log de solo-añadir); encima, una onda con un pico alto que entra y sale aplanada |

**③ Redis**

| Elemento | Texto exacto |
|---|---|
| Rol | **La memoria de amenazas** |
| Cuerpo | Base de datos en memoria (clave-valor) con latencia sub-milisegundo. Mantiene cacheados los Indicadores de Compromiso (IOCs) externos, listos para consultarse al instante. |
| Etiqueta técnica | `EN MEMORIA · CLAVE-VALOR · < 1 ms` |
| Icono | Chip de memoria con una llave; debajo, dos o tres pares `clave → valor` en tipografía mono |

**④ Apache Flink**

| Elemento | Texto exacto |
|---|---|
| Rol | **El cerebro en tiempo real** |
| Cuerpo | Motor de procesamiento de flujos. Consume los datos de Kafka, consulta Redis de forma asíncrona para buscar coincidencias de amenazas —enriquecimiento al vuelo— y etiqueta las alertas antes de enviarlas al almacenamiento final. |
| Etiqueta técnica | `STREAMING · ENRIQUECIMIENTO AL VUELO · ALERTAS ETIQUETADAS` |
| Icono | Engranaje atravesado por una flecha de flujo; a la salida, una etiqueta (tag) roja colgando del evento |

**Nodo final — Almacenamiento final** (sin numerar, estilo más discreto)

| Elemento | Texto exacto |
|---|---|
| Cuerpo | Alertas listas para actuar y eventos conservados a largo plazo para el análisis forense. |
| Icono | Cilindro de base de datos con un pequeño reloj |

Este nodo cierra el círculo con el bloque 01: tiempo real y retención a largo plazo.

#### Franja "¿Por qué desacoplada?"

Tres microbeneficios en una fila, bajo el diagrama:

| Texto exacto | Icono |
|---|---|
| **Resiste.** Si una pieza se detiene, Kafka conserva los eventos. | Escudo |
| **Escala.** Cada capa crece por separado, según su propia carga. | Flechas de expansión |
| **Evoluciona.** Se añaden fuentes nuevas sin rediseñar el flujo. | Pieza de puzle |

---

### Cierre

| Elemento | Texto exacto |
|---|---|
| Frase de remate | **Capturar en el borde. Amortiguar en Kafka. Recordar en Redis. Decidir en Flink.** |
| Línea final | Este es el punto de partida de nuestro proyecto de Big Data aplicado a la Ciberseguridad. |
| Pie | `[Nombre del equipo] · [Asignatura / organización] · [Fecha]` |

**Visual:** los cuatro iconos del bloque 03 en fila, pequeños, unidos por la línea cian que termina en el punto rojo, igual que en la cabecera.

---

## 5. Lista de verificación de contenido

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

## 6. Notas para quien maquete

- **Jerarquía:** el diagrama del bloque 03 es la pieza central y debe ocupar cerca del 45 % de la altura. Los bloques 01 y 02 son el preámbulo que lo justifica.
- **Densidad:** ningún cuerpo de texto supera las tres líneas a ancho de tarjeta. Si no cabe, se recorta el texto, no se reduce la tipografía.
- **Versión horizontal (16:9) para diapositivas:** el mismo contenido se reordena con el bloque 01 a la izquierda, el 02 arriba a la derecha y el diagrama del 03 en horizontal ocupando la franja inferior, con Redis colocado sobre Flink.
- **Precisión técnica del cruce:** Abuse.ch y AlienVault OTX aportan indicadores observables (IPs, dominios, hashes) que se comparan directamente con los eventos. CISA KEV aporta identificadores CVE, que se cruzan con los eventos que reportan vulnerabilidades. Si se ilustran claves de ejemplo en Redis, conviene reflejarlo: `ioc:ip:…`, `ioc:hash:…`, `kev:CVE-…`.
- **Acceso a los feeds:** CISA KEV se publica como JSON abierto. Abuse.ch y AlienVault OTX son gratuitos pero piden una clave de API asociada a una cuenta; conviene confirmarlo antes de planificar la carga programada. No afecta al diseño.
