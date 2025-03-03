# Políticos y firmas chilenas involucradas en casos de evasión (o elusión) de impuestos

El proyecto tratará de buscar conexiones entre figuras influyentes y entidades financieras dedicadas a la elusión de impuestos a través de paraísos fiscales. La base de datos a utilizar es otorgada por la [International Consortium of Investigative Journalist](https://offshoreleaks.icij.org/) y se ocupará la plataforma comunitaria de Neo4J. 

### Conexión al servidor 

Dado que el cluster del servidor estaba siendo utilizado para otro proyecto, se estableció un servidor propio a través de una Raspberry Pi 5. Utilizando las herramientas de *"tunnel port fowarding"* se estableció una conexión SSH a las direcciones IP de los miembros respectivo del grupo. 

Puesto la capacidad limitada del CPU, se modificó el tamaño de los baches y varios otros toques que se pueden encontrar en el archivo de configuración de Neo4J. En específico, para una CPU de 8gb se establecieron los siguientes parámetros; 

```bash
#********************************************************************
# Memory Settings
#********************************************************************
#
# Memory settings are specified kilobytes with the 'k' suffix, megabytes with
# 'm' and gigabytes with 'g'.
# If Neo4j is running on a dedicated server, then it is generally recommended
# to leave about 2-4 gigabytes for the operating system, give the JVM enough
# heap to hold all your transaction state and query context, and then leave the
# rest for the page cache.

# Java Heap Size: by default the Java heap size is dynamically calculated based
# on available system resources. Uncomment these lines to set specific initial
# and maximum heap size.
server.memory.heap.initial_size=2g
server.memory.heap.max_size=3g

# The amount of memory to use for mapping the store files.
# The default page cache memory assumes the machine is dedicated to running
# Neo4j, and is heuristically set to 50% of RAM minus the Java heap size.
# server.memory.pagecache.size=10g

# Limit the amount of memory that all of the running transaction can consume.
# The default value is 70% of the heap size limit.
dbms.memory.transaction.total.max=512m

# Limit the amount of memory that a single transaction can consume.
# By default there is no limit.
db.memory.transaction.max=256m

# Transaction state location. It is recommended to use ON_HEAP.
# db.tx_state.memory_allocation=ON_HEAP

# Tiempo de timeout de la transaccion
db.transaction.timeout=60m
```

Por el otro lado, se habilitó el puerto 7474 para poder utilizar la interfaz gráfica mediante el navegador web. 


