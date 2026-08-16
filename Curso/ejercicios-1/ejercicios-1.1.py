otros_cursos_min = 2.5
otros_cursos_promedio = 4
otros_cursos_max = 7
curso_actual= 1.5

print("----------------------------------------------")
# Diferencias de duracion en procentajes respecto a curso de dalto
diferencia_curso_max = 100 - (curso_actual * 1000 // otros_cursos_max) / 10
diferencia_curso_promedio = 100 - (curso_actual * 100 / otros_cursos_promedio) 
diferencia_curso_min = 100 - (curso_actual * 100 / otros_cursos_min)

print("Un curso dalto dura: ")
print(f" - un {diferencia_curso_max}% menos que el mas lento")
print(f" - un {diferencia_curso_promedio}% menos que el promedio")
print(f" - un {diferencia_curso_min}% menos que el mas rapido")


#Duracion de crudos (tiemp sin edicion)
crudo_promedio = 5
crudo_dalto = 3.5

#Calculando el porcentaje de tiempo vacio removido (para que sea puro contenido de calidad)
tiempo_vacio_promedio = 100 - (otros_cursos_promedio * 100 / crudo_promedio)
tiempo_vacio_dalto = 100 - (curso_actual * 1000 // crudo_dalto) / 10

print("----------------------------------------------")
print(f"El curso promedio tiene un total de {tiempo_vacio_promedio}% de tiempo vacio eliminado del total de grabacion")
print(f"El curso de dalto tiene un total de {tiempo_vacio_dalto}% de tiempo vacio eliminado del total de grabacion")

print("----------------------------------------------")

#A cuentas horas de este curso equivale ver otro curso
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // curso_actual / 10} horas de otros cursos")
#A cuentas horas de otros cursos equivale ver este curso
print(f"Ver 10 horas de otros cursos equivale a ver {curso_actual * 100 // otros_cursos_promedio / 10} horas de este curso")
print("----------------------------------------------")

