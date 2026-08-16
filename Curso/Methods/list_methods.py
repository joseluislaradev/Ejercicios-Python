
#Creando una lista con List

lista = list(["hola", "dalto", 23.6, True]) #Crea un lista, util para crear una lista vacia.
lista2 = [1, 6, 4, 0, 1.65]
print(lista)

resultado = len(lista) #Devuelve el numero de elementos de la lista
print(resultado)

agregando_con_append = lista.append("agregado_append") #Modifica la lista agregando un nuevo elemnto al final, la variable donde guardamos no tiene nada
lista.insert(2, "agregado_insert") #Agrega un elemnento en un indice especifico, el agregado se vuelve dos y mueve el dos al sigueinte
lista.extend([False, "Juan", 2023]) #Agrega varios elemntos a la lista, le pasamos una lista 

print(lista)

del lista[2] #Elimina el elemnto de una lista como pop pero sin devolverlo
eliminado = lista.pop(2) #Elimina un elemento a una lista por su indice y devuelve el que elimino si lo ocupamos, poner -1 elimina el ultimo, -1 no existe asi que se va al ultimo
print("El elemento eliminado es", eliminado)
lista.remove("dalto") #Elimina un elemento de la lista por su valor, sino existe manda un excepcion


#Pasale el parametro reverse=true para ordenarlos al reves
lista2.sort() #Ordena la lista de forma ascendente, no puede tener caracyteres

lista2.reverse() #Invierte los elementos de la lista, ultimo primero y primero ultimo, a diferencia de hacer esto con sort es que sort la ordena y luego lo voltea, reverse lo voltea tal cual

print(lista)
print(lista2)
print(dir(("Hola", 56)))
print(dir(set(["Hola", 56]))) #Creando un conjunto
print(dir(["Hola", 56])) #Creando una lista


my_list = [10,7,9,1,5,2]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1] #Sirve para intercambiar los valores de la lista
print(my_list)
