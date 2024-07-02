#!/bin/bash
NEO4J_BIN=/opt/neo4j/bin

# Cargar relaciones desde archivos CSV
for file in /opt/neo4j/import/relationships-parte-*; do
  echo "Loading $file"
  $NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "CALL {
    LOAD CSV WITH HEADERS FROM 'file:///$file' AS row
    MATCH (startNode {node_id: row.node_id_start}) USING INDEX startNode:Node(node_id)
    MATCH (endNode {node_id: row.node_id_end}) USING INDEX endNode:Node(node_id)
    CREATE (startNode)-[r:REL_TYPE {
      link: row.link,
      status: row.status,
      start_date: date(row.start_date),
      end_date: date(row.end_date),
      sourceID: row.sourceID
    }]->(endNode)
  } IN TRANSACTIONS OF 1000 ROWS;"
done
