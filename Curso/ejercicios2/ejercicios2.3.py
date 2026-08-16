#Creando una funcion que muestre la serie fibonacci entre 0 y el numero dado.

#Mi solucion
num = int(input("Hasta que numero quieres la serie fibonacci: "))

"""
def fibonacci(num):
    serie = [0, 1]
    while True: #Hago que siempre sea true el bucle y va a salir hasta que yo salga desde adentro
        suma = serie[-1] + serie[-2] #Va sumando los ultimos 2 elementos de la lista
        if suma <= num: #Checa que no haya superado el limite que dio el usuario
            serie.append(suma) #Si, no lo guardamos
        else: 
            return serie #Si la suma se paso ya no lo guardamos, y salimos

print(f"La serie es: {fibonacci(num)}")

"""


#Solucion dalto

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b = b, a+b
            
resultado = fibonacci(num)
print(resultado)