c1 = float(input("Ingresa la primera calificacion: "))
c2 = float(input("Ingresa la segunda calificacion: "))
c3 = float(input("Ingresa la tercera calificacion: "))

if c1 >= 8 and c2 >=8 and c3 >=8:
    promedio = (c1 + c2 + c3) / 3
    print("El promedio es: ", promedio)
else: 
    print("Estas reprobado")                         