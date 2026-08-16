#El segundo parametro es una a de "append", permiso para agregar codigo al final del archivo
with open("archivos_txt//texto_joses_agregar.txt","a", encoding="UTF-8") as archivo:
    #Como usamos append solo lo agrega al final, si fuera le permiso write lo sustituye
    archivo.write("Jaja te rebanco\n") #Si no encuentra el archivo, lo crea porque le permiso a
    
    #Usando un bucle para agregar varias lineas
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada\n")
        
    #Usando un bucle en una linea
    [archivo.write(f"Linea en for corto {i+1} agregada\n") for i in range(5)]