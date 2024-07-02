Muchas consultas eran recursivas y requerían de mucha iteraciones. Por el otro lado, el proceso de enlazamiento de datos para obtener la declaración de intereses de los candidatos debía ser automatizado. Por lo mismo, se realizaron diversos ejecutables para correr dentro del servidor (y, en su defecto, dentro de la *cypher-shell*), como también otros programas para poder *"scrapear"* y entrelazar datos. 

## Creación de los nodos y relaciones 

## Entrelazamiento de las declaraciones de interés 
Los datos asociados a los postulantes por las distintas alcaldías se obtuvieron mediante el sitio web de [InfoProbidad](https://www.infoprobidad.cl/Reporte/DetalleDatosHome?Autoridad=CPA2024). 

Para poder obtener un archivo conciso con la información de las acciones de cada candidato, se utilizó la librería `BeautifulSoup` de Python. Cada persona tenía un sitio web asociado, que a su vez, tenía un JSON con todo el patrimonio e información relevante. Por lo mismo, mediante un filtro de los elementos HTML y la utilización de regex se pudo extraer los documentos JSON asociados a cada entidad. 

Por consecuencia, se creó una base de datos MongoDB para poder hacer consultas dentro de cada JSON. En específico, se quería extraer el atributo de las acciones de cada persona. Por lo mismo, mediante la API que ofrece `pymongo`, se hizo una conexión a la consola de MongoDB para poder ejecutar distintas queries de forma iterada. Notar que existían muchos casos donde los aspirantes a alcaldes no tenían ninguna acción declarada. Por lo mismo, se verificó su existencia antes de realizar las respectivas consultas. Por último, las proyecciones se llevaron a un csv con los datos *"normalizados"*, vale decir, por cada aparición de una empresa de algún candidato, se añadía una fila, dando la posibilidad de repetir los nombres. 
