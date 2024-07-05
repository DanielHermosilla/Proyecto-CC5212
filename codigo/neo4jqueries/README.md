Al final, para las importaciones de datos, se utilizó el *bulk-loader* de Neo4J al requerir mucho poder de computación para incluir las relaciones (incluso habiendo creado índices). Por lo mismo, se corrió el siguiente comando, habiendo también editado los CSV al formato requerido para `neo4j-admin`: 

```bash
sudo bin/neo4j-admin database import full --id-type=string --nodes=import/addressesFilter.csv /
--nodes=import/officerFilter.csv /
 --nodes=import/entityFilter.csv /
 --nodes=import/intermediariesFilter.csv /
 --relationships=import/relationshipsFilter.csv /
patos2 --overwrite-destination
```
