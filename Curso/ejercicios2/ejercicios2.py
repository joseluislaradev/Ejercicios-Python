"""Esta fue mi solucion

alumnos_calificacion = []
i = 0

alumnos_cantidad = int(input("¿Cuantos alumnos tiene tu clase?\n"))

while(len(alumnos_calificacion) < alumnos_cantidad):
    calificacion = input(f"Ingresa la calificacion del alumno {i+1}: ")
    calificacion = int(calificacion)
    alumnos_calificacion.append(calificacion)
    i += 1


print(f"Por tanto el profesor sera el de calificacion de {max(alumnos_calificacion)} y el asistente el de calificacion de {min(alumnos_calificacion)} ")

"""

#Solucion de dalto

#Funcion para obtener asistente y al profesor segun la edad
def obtener_compañeros(cantidad_compañeros):
    #creando la lista con los compañeros
    compañeros = []

    # ejecutando un for para pedir informacion de cada compñero
    for i in range(cantidad_compañeros):
        nombre = input("Ingresa el nombre del compañero: ")
        edad = input("Ingresa la edad del compañero: ")
        compañero = (nombre,edad)

        #Agregando informacion a la lista
        compañeros.append(compañero)

    #ordenandolos de menor a mayor segun la edad
    compañeros.sort(key=lambda x:x[1]) #Lo ordena por el segundo parametreo que es la edad(por eso posicion 1) y pues ordena toda la tupla de menor a mayor
     
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre para definir al asistente y profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]

    return asistente,profesor


asistente, profesor = obtener_compañeros(4)

print(f"El profesor es: {profesor} y su asistente es {asistente}")





