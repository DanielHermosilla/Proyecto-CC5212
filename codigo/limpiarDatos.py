import csv
import os

# Definir la ruta del archivo CSV original y el archivo de salida
archivoCSV = "nodes-addresses.csv"
archivoSalida = "cleaned_nodes-addresses.csv"

# Lista para almacenar filas limpias
filasLimpias = []


# Función para limpiar las comillas simples y las comas dentro de las comillas dobles en las columnas address y name
def limpiarFila(row):
    filaLimpia = []
    for idx, col in enumerate(row):
        # Eliminar comillas simples
        col = col.replace("'", "")
        # Reemplazar comas por | dentro de las comillas dobles de las columnas address y name
        if idx in [1, 2]:
            col = col.replace(",", "|")
            col = col.replace('"', "")
        filaLimpia.append(col)
    return filaLimpia


# Abrir el archivo CSV original
with open(archivoCSV, mode="r", newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    filasLimpias.append(header)
    for i, row in enumerate(csvreader, start=1):
        filaLimpia = limpiarFila(row)
        filasLimpias.append(filaLimpia)
        if i <= 5:
            # Verificamos que todo esté bien...
            print(f"Fila {i}: {filaLimpia}")

# Escribir el archivo CSV limpio
with open(archivoSalida, mode="w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(filasLimpias)

print(f"Archivo CSV limpio guardado como {archivoSalida}")

# Verificar si todas las filas tienen el número correcto de columnas
columnaEsperada = 8
with open(archivoSalida, mode="r", newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    for i, row in enumerate(csvreader, start=1):
        if len(row) != columnaEsperada:
            print(
                f"Error en la fila {i}: se encontraron {len(row)} columnas, se esperaban {columnaEsperada}"
            )
