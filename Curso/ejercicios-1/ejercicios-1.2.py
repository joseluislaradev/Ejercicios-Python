texto = input("Por favor escribe un texto para calcular cuanto tiempo tomaria decirla.")

#Obteniendo una lista del texto
palabras = texto.split(" ") 

#Sacando cuantas palabras hay en la lista
palabras = len(palabras)

#Sacand los segundos que le toma decir el texto
segundos = palabras/2

if segundos > 60:
    print("para flaco tampoco te pedi un testamento")
else:
    print(f"El texto tiene {palabras} palabras")
    print(f"El numero de segundos que te tomara decir el texto es: {segundos}")
    print(f"Como dalto habla 30% mas rápido el lo diria en {(30 * segundos / 100) + segundos} segundos")