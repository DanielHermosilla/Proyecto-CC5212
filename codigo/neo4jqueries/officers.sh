#!/bin/bash
NEO4J_BIN=/opt/neo4j/bin

for file in /opt/neo4j/import/nodes-officers-parte-*; do
  echo "Loading $file"
  $NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "CALL {
    LOAD CSV WITH HEADERS FROM 'file:///$file' AS row
    CREATE (:Officer {
      node_id: row.node_id,
      name: row.name,
      countries: row.countries,
      country_codes: row.country_codes,
      sourceID: row.sourceID,
      valid_until: row.valid_until,
      note: row.note
    })
  } IN TRANSACTIONS OF 500 ROWS;"
done
