def dolar_a_argentino(cantidad):
    print(cantidad / .00121)

def argentino_a_dolar(cantidad):
    print(cantidad * .00121)
    
def lectura_datos():
    print("-"*12, "Calculadora de divisas", "-"*12)

    tipo = input("Ingresa el numero 1 Para convetir de dolar a peso argentino. \nIngresa el numero 2 Para convertir de peso argentino a dolar\n")
    cantidad = float(input("Ingresa la cantidad que quieres transformar: "))

    if(tipo == "1"):
        dolar_a_argentino(cantidad)
    elif(tipo == "2"):
        argentino_a_dolar(cantidad)
    else: 
        print("Porfavor, selecciona una opcion validad")

lectura_datos()


    