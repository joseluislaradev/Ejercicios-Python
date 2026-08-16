"""Pra usar pandas tenemosq ue instalarlo, primeramente descargar pip
Par aver si ya tenemos pip se pone py-m pip
Ahora pondemos el sigueinte cmando en el cmd y se isntalara: py -m pip install pandas"""
import pandas as pd 

df = pd.read_csv("archivos_csv//datos.csv")
df2 = pd.read_csv("archivos_csv//datos.csv")

#df = pd.read_csv("archivos_csv//datos.csv", names=["name", "lastname", "age"]) 

#Imprime toda la info
print(df)

#obteniedno los datos de la columna nombre
print(df["Nombre"])

#Slicing es una tecnica en python que nos permite hacer diversas cosas dependiendo dependiendo del objeto
cadena = "0123456789"
print(cadena[:]) #Nos permite definir un principio o un final al trbaajr con un array, aqui no hay principio ni final asi que impirme todo
print(cadena[2:8]) #empiezca desde el elemnto dos hasta el 8 (la posicion final no va incluido en la impresion).

df_ordenado = df.sort_values("Edad", ascending=False) #Ordenando los valores de manera descendiente 
print(df_ordenado)

#Concatenando 2 dataframes
df_concatenado = pd.concat([df, df2])
print(df_concatenado)

#Accediendo a las filas de arriba a abajo
primer_fila = df.head(1) #Muestra las primera fila de nuestro dataframe, si cambiamos el nuemro podemos hacer que muestre mas o menos filas
print(primer_fila)

#Accediendo a las filas de abajo a arriba
ultima_fila = df.tail(1) #Muestra la ultima fila de nuestro dataframe, si cambiamos el nuemro podemos hacer que muestre mas o menos filas
print(ultima_fila)

filas_y_columnas = df.shape #Develve la cantidad de filas y columnas del dataframe en una tupla
print(filas_y_columnas)

#Obteniendo informacione stadistica(como desviacion estandar, min, max, cantidad etc.)
df_info = df.describe()
print(df_info)

#Accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2, "Edad"] #Se pone primero el indice de la fila(el numero que se le asigna automaicamente a cada fila), despues la columna especifica a la que queremos acceder.

#Accediendo a todas las filas de un columna
fila_1 = df.loc[1, :] #De filas pone la 1, de columas pone todas

#Accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2, 2] #Se ponen solo los indices especificos del elemento

#Accediendo a todas las filas de un columna
apellidos = df.iloc[:, 1] #De filas pone todas (:), de columas solo la de indice 1 que es la de apellido


print(elemento_especifico_loc)
print(fila_1)
print(elemento_especifico_iloc)
print(apellidos)

#Accediendo a las filas que tengan la edad mayor a 19
mayor_que_19 = df.loc[df["Edad"] > 19, :] #Solo las filas qeu sean mayores a 19, de columnas todas (:)
print(mayor_que_19)


"""
En uvento es cualquier cosa que sucede en nuestro porgrama, cualquier suceso que sucede como picar un boton del teclado, mover mouse, etc. 
En los lenguajes de programacion captamos los eventos para actuar en consecuencia, como cuando pedimos al usuario que digite un numero


Las excepciones son eventos que ocurren en nuestro programa y captan cuando suceden errores interrumpiendo el flujo normal de ejecucion, 
que sabiendo manejarlas no interrumpen el flujo"""
