#Cambiar el tipo de dato de una columna

import pandas as pd
df = pd.read_csv("archivos_problemas_simples//datos.csv")

#Conviertiendo los datos de una columna a string
df["edad"] = df["edad"].astype(str)
print(type(df["edad"][0]))

#Reemplazando dato especifico por otro
df["apellido"].replace("Juarez", "Martinez", inplace=True)
print(df["apellido"])

#Elimina las filas con datos faltantes
df = df.dropna() #Si adentro agregamos "axis=1" se eliminan las columnas con datos faltantes, por defecto son las filas
print(df)

#Eliminando las filas repetidas
df = df.drop_duplicates()
print(df)

#Creando un csv con el dataframe nuev
df.to_csv("archivos_problemas_simples//datos_limpios.csv")



