#El segundo parametro es una w de "write", permiso para escribir en el archivo
with open("archivos_txt//texto_joses.txt","w", encoding="UTF-8") as archivo:
    #Aqui sobreescribe la informacin
    archivo.write("Jaja te rebanco\n") #Si no encuentra el archivo, lo crea poque le permiso w

    #Aqui no sobreescribe la informacion
    archivo.writelines(["Hola como estas\n", "Alto crack\n"]) #Inverso a readlines que devuelve una lista con todas las lineas, con writelines le pasamos una lista y las escribe en el archivo