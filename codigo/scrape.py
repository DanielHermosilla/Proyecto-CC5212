import csv
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import urllib3  # Desactivar los warnings por no tener certificado SSL...

# Sacar Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

alcaldes = pd.read_csv("candidatos.csv")

print(alcaldes["Declaracion"])

respuestasJson = []
for link in alcaldes["Declaracion"]:
    # El contenido de la web lo toma como malicioso, por eso no se verifica
    response = requests.get(link, verify=False)

    soup = BeautifulSoup(response.text, "html.parser")
    # Suponiendo que 'response_text' es el texto HTML obtenido
    tabla = soup.find_all("table", class_="description")

    # Unión de los strings contenidos en las tablas
    table_texts = [table.text for table in tabla]
    response_text = "\n".join(table_texts)

    # Regex para filtrar los JSON
    pattern = re.compile(
        r"({.*})", re.DOTALL
    )  # que busca cualquier contenido entre llaves

    # Buscar el JSON en el texto
    match = re.search(pattern, response_text)

    if match:
        json_data = match.group(1)  # Obtener el grupo capturado que corresponde al JSON
        respuestasJson.append(json_data)
    else:
        respuestasJson.append(None)

alcaldes["respuestaJson"] = respuestasJson

alcaldes.to_csv("candidatos_json.csv", index=False)
