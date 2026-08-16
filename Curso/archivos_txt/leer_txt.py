#UNn archivo es un contenedor de informacion que puede ser se vaiuros tipos, 
# wap para audio, mp4 para video, txt para texto plano

#Leer archivo completo
archivo_sin_leer = open("archivos_txt\\texto_jose.txt", encoding="UTF-8") #Primero la carptea contenedora y despues el archivo a abrir, encoding UTF-8 es la codificacion universal para que salgan todos los caracteres
archivo_leido = archivo_sin_leer.read()

print(dir(archivo_sin_leer))
print(archivo_sin_leer.read()) 

print(archivo_leido)

#Cuando un archivo se lee, para poder volver a leerlo tenemos que cerrarlo, la compu libera los recursos
archivo_sin_leer.close()

#Leer linea por linea
archivo_sin_leer = open("archivos_txt\\texto_jose.txt", encoding="UTF-8") #Primero la carptea contenedora y despues el archivo a abrir, encoding UTF-8 es la codificacion universal para que salgan todos los caracteres
lineas = archivo_sin_leer.readlines() #Devuelve una lista con cada linea del archivo, no se recomienda en archivos grandes porque puede consumir todas la memoria ram de computador
print(lineas)

archivo_sin_leer.close()
archivo_sin_leer = open("archivos\\texto_jose.txt", encoding="UTF-8") #Primero la carptea contenedora y despues el archivo a abrir, encoding UTF-8 es la codificacion universal para que salgan todos los caracteres

#leer una sola liena
lineas = archivo_sin_leer.readline() #Si ponemos un numero adentro leemos solo la cantidad de caracteres que le ponemos
print(lineas)