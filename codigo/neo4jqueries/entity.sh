#!/bin/bash
NEO4J_BIN=/opt/neo4j/bin

# Eliminar índices existentes
$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "DROP INDEX entity_node_id_index IF EXISTS;"
$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "DROP INDEX addresses_node_id_index IF EXISTS;"
$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "DROP INDEX intermediaries_node_id_index IF EXISTS;"
$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "DROP INDEX officers_node_id_index IF EXISTS;"
$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "DROP INDEX other_node_id_index IF EXISTS;"
echo "Se dropearon todos los indices"

# Entity
$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "CREATE INDEX entity_node_id_index FOR (n:Entity) ON (n.node_id);"
# Addresses
$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "CREATE INDEX addresses_node_id_index FOR (n:Addresses) ON (n.node_id);"
# Intermediaries
$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "CREATE INDEX intermediaries_node_id_index FOR (n:Intermediaries) ON (n.node_id);"
# Officers
$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "CREATE INDEX officers_node_id_index FOR (n:Officer) ON (n.node_id);"
# Other
$NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "CREATE INDEX other_node_id_index FOR (n:Other) ON (n.node_id);"
