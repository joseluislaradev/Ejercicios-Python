def frase(nombre, apellido, adjetivo): #Tambien se pueden poner valores directamente aqui para no tener que pasarlos, pero si se pasan se cambian por el que pasamos
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

print(frase(adjetivo="Capo", nombre = "Jose Luis", apellido="Arredondo", )) #Parametro de palabra clave, le indicamos exactamente que vlaor tendra cada parramtro y asi podemos cambiarlo de lugar, los otros son parametro posicionales