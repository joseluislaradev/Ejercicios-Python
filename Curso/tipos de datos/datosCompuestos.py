#Los datos compuesto son un conjunto de datos (es un dato compuesto por otros datos), como los arrays en c++, solo que aqui pueden ser de cualquier tipo
#Las listas, las tuplas, conjuntos y diccionarios son tipos de datos compuestos

lista = ["Jose Luis", "Me gusta el futbol", True, 1.65]
print(lista[3])
tupla = ("Jose Luis", "Me gusta el futbol", True, 1.65) #lo mismo que una lista pero no se puede modificar ni agregar, se puede refefinir completamente

#tupla[3] = "Jan"
print(tupla[3])


conjunto = {"Jose Luis", "Me gusta el futbol", True, 1.65, "Jose Luis"} #no muestra repetidos, no se puede acceder por indice, se puede refefinir
conjunto = {"hola jajajajja"} 

# print(conjunto[3]) #no puede mostrar el elemento
print(conjunto)  #muestra todo el conjunto

#Los datos de una tupla y lista son ordenados, los muestra tal cual esta definidos, los conjuntos no entenodnce los muestra aleatoriamente a como los definimos

#creando un diccionario (es un JSON) se accede con clave-valor
diccionario = {
    'nombre' : "Jose Luis",
    'deporte' : "Futbol", 
    'estado_emocionado' : "True",
    'altura' : 1.65,
    'dato_duplicado' : "Jose Luis"
}

print(diccionario['nombre'] + " bienvenido") #Esta forma de acceder al diccionario crea una excepcion si no se encuentra el elemento