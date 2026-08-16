edades_sin_repetir = []

for i in range(5):
    edad = int(input(f"Ingresa la edad del usuario {i+1}: "))
    if edad not in edades_sin_repetir:
        edades_sin_repetir.append(edad)
    
 
print(f"En el grupo de IGSOFT hay alumnos de {[x for x in edades_sin_repetir]} años de edad")