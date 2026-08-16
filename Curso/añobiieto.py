print("Programa el cual indica si un año es bisiesto")
año = int(input("Ingresa un año "))

while año >= 1582:

    if (año % 4) != 0:
        print(año, "no es un año bisiesto")
    elif (año % 100) != 0:
        print(año, "es un año bisiesto")
    elif (año % 400) != 0:
        print(año, "no es un año bisiesto")
    else :
        print(año, " es un año bisiesto")

    print("Para salir ingresa un año menor a 1582")
    año = int(input("Ingresa un año "))
