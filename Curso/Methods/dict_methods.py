diccionario = {
    "nombre" : "Jose Luis",
    "apellido" : "Lara",
    "subs" : 1000000,
}

print(dir(diccionario))

claves = diccionario.keys() #Obtiene las keys del diccionario
obtener = diccionario.get("apellido") #Le pasamos una key y obtiene su valor, si un elemento no se encuentra envia none
print(diccionario["apellido"]) #da error si no lo encuentra

diccionario.update({"apellido": "Juan"}) #si no existe la clave a actualizar, la agrega al final

diccionario.pop("nombre") #Elimina elementos del diccionario y puede devolver al que elimino, con del solo se elimina y fin
#.popitem() elimina el ultimo elemento de el diccinario
diccionario_iterable = diccionario.items() #Para poder iterar el diccionario

#diccionario.clear() #Elimina todos los elementos del diccionario

print(diccionario)
print(diccionario_iterable)
print(claves)
print(obtener)

