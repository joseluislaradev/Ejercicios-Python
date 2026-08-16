#Las funciones son fragmento de codigo que ya tiene el lenguaje por defecto para ejecutar algo
# en la funciones hay algo que se llama abstraccion y por esto no hace falta que sabramos que hacen exactamente las funciones por dentro, por si si sabemos que hace la funcion y como afecta al programa no hace falta saberlo
#Ayuda a la moduralidad- Separar el programa en partes mas pequeñas, podemos probarlas por separado y despues integrarlas de nuevo al programa
#Reutilizacion de codigo - Sin hacer copy paste solo haceindo referencia a la funcion
#Mas facil de mantener y modificar porque sabemos donde esta todo
#El codigo es mas legible - Todo esta mas separado

#Las funciones que tre python por defecto se llaman built-in, aunque podemos crer las propias

numeros = [2,6,7,1,89,3]

#Muestra el numero mayor de una lista
numero = max(numeros)
print(numero)

#Muestra el numero mayor de una lista
numero = min(numeros)
print(numero)

#Redondea un numero a 6 decimales
#Muestra el numero mayor de una lista
numero = round(56.499344, 5) #Sin poner lo decimales qeu se quieren, apartir de .5 redondea hacia arriba de .4 hacia abajo. El primer argumento es el numero a deondear y el segundo la cantidad de deciameles, si ponemos dos solo muestra uno porque sel segundo es el que redondea
print(numero)

#retorna false, si lo que le pasamos esta completamente vacia, el falsa, none, o 0, como una lista toda vacia, etc
resultado_bool = bool([])
print(resultado_bool)

#retrona false, si algun elemento de un iterable (una lista, tupla, etc) esta vacio, es 0, False o None y retorna TRue si todo es verdadero
resultado_all = all([1, 0, "hello", ["344", "Jose"]])
print(resultado_all)

#Suma todos los vlores de un iterable
suma_total = sum(numeros)
print(suma_total)



