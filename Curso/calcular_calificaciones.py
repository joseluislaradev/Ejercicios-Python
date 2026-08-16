calculo = float(input("Ingresa la calificacion de la materia de calculo: "))
redes = float(input("Ingresa la calificacion de la materia de redes: "))
ciencias = float(input("Ingresa la calificacion de la materia de ciencias: "))

promedio = (calculo + redes + ciencias) / 3

if(promedio < 8.0):
    print("Tu calificacion es un  NA")
elif 8.0 < promedio < 8.4:
    print("Tu calificacion es un SA")
elif 8.5 < promedio < 9.4:
    print("Tu calificacion es un DE")
else:
    print("Tu calificacion es un AU")
    
"""
if promedio >= 9.5:
    print("Tu calificaciones es un AU")
elif 8.5 <= promedio < 9.5 :
    print("Tu calificacion es un DE")
elif 8.0 <= promedio < 8.5:
    print("Tu calificacion es un SA")
else:
    print("Tu calificacion es un NA")
"""