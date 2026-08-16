frutas = ["manzana", "pera", "ciruela", "naranja", "granada", "durazno"]
cadena = "Hola Jose Luis"
numeros = [1,2,3,4,5]

for fruta in frutas:
    if(fruta == "granada"):
        continue #Esta instruccion se salta el ciclo actual en el momento que se ejecuta, si va en la iteracion 3 y sale continue ingnora lo que sigue y pasa a la iteracion 4
    print(f"Me voy a comer una {fruta}")
    
for fruta in frutas:
    if(fruta == "naranja"):
        print("La naranja me hizo daño")
        break #Termina el bucle sin importar cuantas iteraciones falten, tambien se salta el else
    print(f"Me voy a comer una {fruta}")
else:
    print("Bucle terminado")

print("Bucle terminado 2")

for letra in cadena:
    print(letra)
    
    
#for en una sola linea de codigo
#Primero en muchas
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)

print(numeros_duplicados)

#Una sola
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

