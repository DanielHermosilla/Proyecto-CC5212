import pandas as pd

def clean_csv(file_path, output_path, id_column):
    df = pd.read_csv(file_path)
    df_clean = df.drop_duplicates(subset=id_column)
    df_clean.to_csv(output_path, index=False)
    print(f"Archivo limpio guardado en {output_path}")

# Guardar los datos sin repeticiones dentro del mismo label

clean_csv('/opt/neo4j/import/addressesF.csv', '/opt/neo4j/import/addressesF.csv', 'node_id:ID')
clean_csv('/opt/neo4j/import/officerF.csv', '/opt/neo4j/import/officerF.csv', 'node_id:ID')
clean_csv('/opt/neo4j/import/entityF.csv', '/opt/neo4j/import/entityF.csv', 'node_id:ID')
clean_csv('/opt/neo4j/import/intermediariesF.csv', '/opt/neo4j/import/intermediariesF.csv', 'node_id:ID')
clean_csv('/opt/neo4j/import/relationshipsF.csv', '/opt/neo4j/import/relationshipsF.csv', 'node_id:ID')

# Eliminar duplicados dentro de TODOS los labels
df1 = pd.read_csv('/opt/neo4j/import/addressesF.csv')
df2 = pd.read_csv('/opt/neo4j/import/officerF.csv')
df3 = pd.read_csv('/opt/neo4j/import/entityF.csv')
df4 = pd.read_csv('/opt/neo4j/import/intermediariesF.csv')
df5 = pd.read_csv('/opt/neo4j/import/relationshipsF.csv')
combined_ids = pd.concat([df1['node_id:ID'], df2['node_id:ID'], df3['node_id:ID'], df4['node_id:ID']])
duplicated_ids = combined_ids[combined_ids.duplicated()].unique()

df1_filtered = df1[~df1['node_id:ID'].isin(duplicated_ids)]
df2_filtered = df2[~df2['node_id:ID'].isin(duplicated_ids)]
df3_filtered = df3[~df3['node_id:ID'].isin(duplicated_ids)]
df4_filtered = df4[~df4['node_id:ID'].isin(duplicated_ids)]

df1_filtered.to_csv("addressesFilter.csv", index=False)
df2_filtered.to_csv("officerFilter.csv", index=False)
df3_filtered.to_csv("entityFilter.csv", index=False)
df4_filtered.to_csv("intermediariesFilter.csv", index=False)

ids_final = combined_ids[~combined_ids.isin(duplicated_ids)].unique()

# Eliminar nodos fantasmas en relationships 
print("Empieza a filtrar los csvd e Relationships")
df5 = df5[~df5[':START_ID'].isin(duplicated_ids) & ~df5[':END_ID'].isin(duplicated_ids)]
df5_filtered = df5[df5[':START_ID'].isin(ids_final) & df5[':END_ID'].isin(ids_final)]

df5_filtered.to_csv("relationshipsFilter.csv", index=False)
print("Se guardaron los csv")
