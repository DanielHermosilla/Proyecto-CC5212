Muchas consultas eran recursivas y requerían de mucha iteraciones. Por el otro lado, el proceso de enlazamiento de datos para obtener la declaración de intereses de los candidatos debía ser automatizado. Por lo mismo, se realizaron diversos ejecutables para correr dentro del servidor (y, en su defecto, dentro de la *cypher-shell*), como también otros programas para poder *"scrapear"* y entrelazar datos. 

## Limpieza los datos

Algunos archivos que tenían los datos para cada nodo venían mal formateados. Habían errores con las commas y comillas doble. Por lo mismo, también se generó un archivo python para limpiar tales errores bajo el archivo `limpiar.py`

Por el otro lado, también nos encontramos con unos pocos nodos $(\approx 10^3)$ que estaban repetidos y hacían que se generen choques entre "IDs". Además, algunas relaciones también hacían alusión a "ID's" que no existían. Esto fue arreglado bajo con Pandas en el archivo `limpiarRepetidos.py` 

## Creación de los nodos y relaciones 

Dado el tamaño de los heaps, no era posible subir todos los nodos de una única transacción. Por lo mismo, se utilizó la función `CALL {} IN TRANSACTION OF 500 ROWS;` para cada CSV (encontrado en /opt/neo4j/imports) que contenía los nodos. Por el otro lado, aquellos archivos que contenían más de $10000$ entradas fueron divididos en archivos más pequeños para poder procesar las transacciones. Dado la gran cantidad de entradas, se realizó el siguiente script que automatizaba la subida de datos en el cypher-shell; 

```bash
#!/bin/bash
NEO4J_BIN=/opt/neo4j/bin

for file in /opt/neo4j/import/parte-*; do
  echo "Loading $file"
  $NEO4J_BIN/cypher-shell -u neo4j -p danielpatos "CALL {
    LOAD CSV WITH HEADERS FROM 'file:///$file' AS row
    CREATE (:Entity {
      node_id: row.node_id,
      name: row.name,
      original_name: row.original_name,
      former_name: row.former_name,
      jurisdiction: row.jurisdiction,
      jurisdiction_description: row.jurisdiction_description,
      company_type: row.company_type,
      address: row.address,
      internal_id: row.internal_id,
      incorporation_date: row.incorporation_date,
      inactivation_date: row.inactivation_date,
      struck_off_date: row.struck_off_date,
      dorm_date: row.dorm_date,
      status: row.status,
      service_provider: row.service_provider,
      ibcRUC: row.ibcRUC,
      country_codes: row.country_codes,
      countries: row.countries,
      sourceID: row.sourceID,
      valid_until: row.valid_until,
      note: row.note
    })
  } IN TRANSACTIONS OF 500 ROWS;"
done
```

Por el otro lado, para poder generar los nodos de relaciones se tuvo que crear índices para cada identificador único del nodo. Así, optimizar el proceso para la computación limitada que se tenía. 

Tras complejidades con la subida de las relaciones, se reemplazó el método de subida con el *bunk loader* de Neo4J con el `neo4j-admin import database`. Como ganancia, los datos se subieron de forma más eficiente $(\approx 140s)$. Como pérdida, se perdió el control o la flexibilidad que otorga Neo4J para subir nodos desde el cypher-shell. 

## Entrelazamiento de las declaraciones de interés 
Los datos asociados a los postulantes por las distintas alcaldías se obtuvieron mediante el sitio web de [InfoProbidad](https://www.infoprobidad.cl/Reporte/DetalleDatosHome?Autoridad=CPA2024). 

Para poder obtener un archivo conciso con la información de las acciones de cada candidato, se utilizó la librería `BeautifulSoup` de Python. Cada persona tenía un sitio web asociado, que a su vez, tenía un JSON con todo el patrimonio e información relevante. Por lo mismo, mediante un filtro de los elementos HTML y la utilización de regex se pudo extraer los documentos JSON asociados a cada entidad. 

Por consecuencia, se creó una base de datos MongoDB para poder hacer consultas dentro de cada JSON. En específico, se quería extraer el atributo de las acciones de cada persona. Por lo mismo, mediante la API que ofrece `pymongo`, se hizo una conexión a la consola de MongoDB para poder ejecutar distintas queries de forma iterada. Notar que existían muchos casos donde los aspirantes a alcaldes no tenían ninguna acción declarada. Por lo mismo, se verificó su existencia antes de realizar las respectivas consultas. Por último, las proyecciones se llevaron a un csv con los datos *"normalizados"*, vale decir, por cada aparición de una empresa de algún candidato, se añadía una fila, dando la posibilidad de repetir los nombres. 

## Consultas en Neo4J 

Dado que muchas consultas tenían que ser automatizadas, se utilizaron muchos códigos bash para poder ir iterando entre las distintas figuras de interés.

