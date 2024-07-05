#!/bin/bash

NEO4J_BIN=/opt/neo4j/bin

# Chilenos involucrados en las filtraciones
$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "
MATCH (p:Officer)-[]-(c:Addresses)
WHERE 'Chile' IN c.countries
RETURN p.name, c.address;
"
echo "Busqueda por chilenos involucrados en las filtraciones y sus direcciones"

$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "
MATCH (a:Addresses)
RETURN a.country_codes, COUNT(*) AS count
ORDER BY count DESC;
"
echo "Mayor cantidad de países involucrados."

$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "
MATCH (x:Addresses {country_codes: 'CHL'}) RETURN x.address;
"
echo "Las direcciones de aquellas personas involucradas"

$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "
MATCH (p:Entity)-[]-(c:Addresses)
WHERE 'Chile' IN c.countries
RETURN p;
"
echo "Tipo de entidades involucradas"
