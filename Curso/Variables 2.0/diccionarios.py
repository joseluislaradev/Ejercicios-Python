#creando diccionario con dict()
diccionario = dict(nombre="jose", apellido="lara")

#las listas no pueden ser claves porque son mutables, pero tuplas si, tambien un conjunto como frosenset, nomral no
diccionario = {
    ("dalto", "rancio"):"jajaja",
    #["dalto", "rancio"]:"jajaja" #No se puede por ser lista
}

#creando diccionario con fromkeys(), esto crea un diccionario 
diccionario = dict.fromkeys("nombre", "apellido") #Asi le da a cada letra del primer argumento, en este caso cada letra de nombre sera un elemento y tendra el valor el segundo parametreo, es decir "apellido", si no se da el segundo parametro es none, esto funciona asi porque el primer elemento lo convierte en iterable
print(diccionario) 

diccionario = dict.fromkeys(["nombre", "apellido"]) #Mnadar una lista para que cree un elemeneto de diccionario con cada elemento de la lista pero con valor none, si le agregamos eegundo parametro les da ese valor
print(diccionario) 