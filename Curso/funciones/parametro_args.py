#Forma no óptima de hacer una suma
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados += numero
    return numeros_sumados

resultado = suma([5,7,1,9,10,6])
print(resultado)


#Forma optima utilizando el parametro args como argumento, nos permite mandar muchas varibales con tan solo poner un asterisco enfrente y actua como tupla

def suma_optima(nombre, *numeros): #No se pueden aagregar mas parametros despues de args tiene que ir antes
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"  #El parametro args trata a los elementos como tupla

resultado = suma_optima("Jose Luis", 5, 6, 8, 1, 0, 1, 5)
print(resultado)


#Uitlizando args diferente

def suma_total(numeros):
    print(*numeros, sep=", ", end=".\n")
    return sum([*numeros]) #Args es un tipo de datos especial, no retorna nada al ponerlo en la funcion type, si convertimos una lista a args con el asterisco obtiene los valores de una lista pero sin ser lista al imprimrilso

resultado2 = suma_total([5, 6, 8, 1, 0, 1, 5])
print(resultado2)


"""
La diferencia de usar una lista y usar args como parametro es: 
1. Si una lista es mutable y se modifica algun valor dentro de la funcion persistira afuera de la funcion. 
    ARGS puede aceptar una captidad variable de argumentos y los trata como una tupla 
2. Mejora legibilidad del codigo pasando puros argumentos individuales sin tener que crear una lista para 
    despues pasarla  a la funcion.
"""