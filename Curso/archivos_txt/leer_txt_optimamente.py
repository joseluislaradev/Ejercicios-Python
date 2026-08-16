with open("archivos_txt//texto_jose.txt", encoding="UTF-8") as archivo: #Se abre un archivo, se ejecutan las instrucciones dentro y se cierra solo una vez termiandas
    print(archivo)
    print(archivo.read())
    print("Hola con print")