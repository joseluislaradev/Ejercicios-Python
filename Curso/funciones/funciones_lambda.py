"""Lambda es una forma de crear una funcion anonima, es decir, sin nombre
1. Sirve para cuando se quiere hacer algo sencillo y rapido puesto que ahorra lineas de codigo,
no son aptas cuando tenemos que hacer mas de una instruccion"""

multiplicar_por_dos = lambda x : x*2 #Almacenando una funcion en una variable

print(multiplicar_por_dos(5))

#La funcion filter sirve para devolvernos true o false en cada elemento de algo, y devuelve en forma de lista todos los elementos de la lista en que la funcion era true
numeros = [1,2,3,4,5,6,7,8,9,10]

#Definiendo una funcion normal y haciendo uso de filter para ver que numeros son pares

def es_par(num):
    if(num%2 == 0):
        return True

numeros_pares = filter(es_par,numeros) #tiene dos parametros, primero la funcion que verificara, y luego la lista que recorrera y sometera cada elemento a la fucnion dada
print(numeros_pares) #Numeros_pares es un objeto filter, para poder mpirmir los valores que dieron true se tiene que convertir a lista
print(list(numeros_pares)) #Conviertiendo objeto filter a lista


#Haciendo lo mismo de arriba pero con lambda
numeros_pares = filter(lambda x : x%2 == 0,numeros) #La funcion la tiene directamente en una linea con lambda, pasa cada elemento de la lista numeros por la funcion y las que den true las guarda
print(numeros_pares) 
print(list(numeros_pares)) 

