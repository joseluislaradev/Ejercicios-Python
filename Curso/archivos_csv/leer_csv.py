
"""Esto lee el archivo como si fuera txt
with open("archivos_csv//datos.csv") as archivo:
    print(archivo.read())
    print("Datos leidos correctamente")
"""

#Para el ambito profesional dalto no nos recomienda trabajar con este modulo si no con pandas que es mucho ams completo
import csv

with open("archivos_csv//datos.csv") as archivo:
    reader = csv.reader(archivo)
    print(reader) #Imprime un objeto csv el cual es un iterable,se le llaama dataframe porque tiene filas y columans
    
    for row in reader: #Recorriendo las filas de iterable reader
        print(row)
        
