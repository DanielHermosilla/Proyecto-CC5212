#!/bin/bash

# Ruta al archivo CSV
archivo_csv=/opt/neo4j/import/alcaldesFinal.csv
NEO4J_BIN=/opt/neo4j/bin

# Omitir la primera linea (encabezados) y luego iterar sobre cada fila
tail -n +2 "$archivo_csv" | while IFS=, read -r columna1 columna2 columna3
do
    $NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "
    MATCH (n:Officer)-[]-(a:Entity)
    WHERE '$columna2' IN n.name OR '$columna3' IN a.name
    RETURN a.nombre;
    "
    echo "Subiendo para $columna2 en la iteracion $columna1"
done
