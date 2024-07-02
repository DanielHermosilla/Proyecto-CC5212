import pandas as pd
import pymongo
import json


# Leer el CSV
alcaldes = pd.read_csv("candidatos_json.csv")

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["patos"]
collection = db["candidatos"]


def insertar():
    # Insertar los JSON en MongoDB
    for json_str in alcaldes["respuestaJson"]:
        try:
            json_data = json.loads(json_str)
            collection.insert_one(json_data)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")

    print("Datos insertados en MongoDB.")


# Consulta en PyMongo
query = {"Derechos_Acciones_Chile": {"$exists": True}}
projection = {
    "Derechos_Acciones_Chile.Nombre_Razon_Social": 1,
    "Datos_del_Declarante.nombre": 1,
    "Datos_del_Declarante.Apellido_Paterno": 1,
    "_id": 0,
}

cursor = collection.find(query, projection)

# Lista para almacenar los datos
data = []
# Iterar sobre los resultados y construir la lista de datos
for document in cursor:
    nombre = f"{document['Datos_del_Declarante']['nombre']} {document['Datos_del_Declarante']['Apellido_Paterno']}"

    # Verificar si 'Derechos_Acciones_Chile' es una lista
    if isinstance(document["Derechos_Acciones_Chile"], list):
        for item in document["Derechos_Acciones_Chile"]:
            if "Nombre_Razon_Social" in item:
                empresas = item["Nombre_Razon_Social"]
                data.append((nombre, empresas))
    else:  # 'Derechos_Acciones_Chile' es un diccionario
        if "Nombre_Razon_Social" in document["Derechos_Acciones_Chile"]:
            empresas = document["Derechos_Acciones_Chile"]["Nombre_Razon_Social"]
            data.append((nombre, empresas))

# Crear el DataFrame
df = pd.DataFrame(data, columns=["Nombre", "Empresas"])

df.to_csv("alcaldesFinal.csv")
# Mostrar el DataFrame
