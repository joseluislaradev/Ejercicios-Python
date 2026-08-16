animales = ["gato", "perro", "loro", "leon"]
numeros = {52, 26, 78, 90}

for animal in animales: #Crea un bucle for en donde cada elemento lo itera con el nombre animal de la lista animales, en cada vuelta va a otro elemento, como un foreach en php
    print("Ahora la variable animal es igual a: " + animal)
    
for numero in numeros:
    print(f"El cuadrado del numero es: {numero**2}")
    
#Iterando dos listas a la vez (tienen que ser del mismo tamaño)
for numero,animal in zip(numeros, animales):
    print(f"Recorriendo la lista 1: {numero}")
    print(f"Recorriendo la lista 2: {animal}")

#Forma no correcta de recorrer una lista con su indice (no funciona en conjuntos ya que no se puede acceder por indice a conjuntos)
for num in range(len(numeros)): #Dentro de range va un numero que es el rango en el que se mostraran los numeros, como 5,10 y seria 5,6,7,8,9
    print(numeros[num])
    
    
#Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    print(num) #Asi se impirme indice y valor, En cada iteracion es una tupla, la cual contiene dos elementos, le primero el numero del indice y su valor
    print(num[0]) #Num(que es una tupla) en su posicion 0 seria el indice
    print(num[1]) #Num(que es una tupla) en su posicion 1 seria el valor
    
for i,num in enumerate(numeros):
    print(f"El indice {i} tienen el valor {num}") #Desempaqueta directamente la tupla en el for, tneemos dos variables, i que guarda el indice e num que guarda el valor del indice, esto porque sabemos que enumerate() devuelve una tupla en cada iteracion con esos dos valores 


#for usando else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle,valor actual: {numero}")
else: #Aunque no se recorra nada en e bucle si hay un else se pasa a el al final del bucle
    print("El bucle termino")