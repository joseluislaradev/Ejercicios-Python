figura = int(input("Ingresa un numero para calcular el area de un: \n 1. Triangulo. \n 2. Rectangulo \n 3. Cuadrado \n 4. Circulo \n "))

def triangulo(dato1, dato2):
    print(f"El resultado es: {(dato1*dato2)/2}")

def rectangulo(dato1, dato2):
    print(f"El resultado es: {dato1*dato2}")

def cuadrado(dato1):
    print(f"El resultado es: {dato1**2}")
    
def circulo(dato1):
    print(f"El resultado es: {3.1416*(dato1**2)}")

if figura == 1:
    dato1 = int(input("\nIngresa la base del triangulo: "))
    dato2 = int(input("Ingresa la altura del triangulo: "))
    triangulo(dato1, dato2)
elif figura == 2:
    dato1 = int(input("\nIngresa la base del rectangulo: "))
    dato2 = int(input("Ingresa la altura del rectangulo: "))
    rectangulo(dato1, dato2)
elif figura == 3:
    dato1 = int(input("\nIngresa el lado del cuadrado: "))
    cuadrado(dato1)
elif figura == 4:
    dato1 = int(input("\nIngresa el radio del circulo: "))
    circulo(dato1)