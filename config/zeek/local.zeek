# Salida de los logs de Zeek en JSON, una línea por evento.
#
# Instalación en el sensor de red:
#   1. Añadir la línea de abajo al final de /opt/zeek/share/zeek/site/local.zeek
#   2. sudo zeekctl deploy
#
# Zeek escribirá las conexiones en /opt/zeek/logs/current/conn.log.
# Esa carpeta es la que hay que montar en el contenedor de Vector
# en lugar de ./logs/zeek (ver docker-compose.yml).

@load policy/tuning/json-logs.zeek
