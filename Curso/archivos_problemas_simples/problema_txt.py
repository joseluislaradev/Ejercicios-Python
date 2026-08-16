#Tenmos dos listas, una con nombre y una con apellido. Tenemos que escirbirlos en un archivo txt de forma optyima con un for

nombres = ["Jose Luis", "Juan", "Pedro", "Armando"]
apellidos = ["Arredondo", "Mancera", "Martinez", "Rodriguez"]
edad = [20, 18, 27, 7]

with open("archivos_problemas_resueltos//problema_txt.txt", "w", encoding="UTF-8") as archivo:
    archivo.writelines("Los datos son: \n\n")
    archivo.writelines([f"Nombre: {n} \nApellido: {a} \n--------------------\n" for n, a in zip(nombres, apellidos)])   


with open("archivos_problemas_resueltos//datos.csv", "w", encoding="UTF-8") as archivo:
    archivo.writelines('"nombre","apellido","edad"\n')
    archivo.writelines([f'"{n}","{a}",{e}\n' for n, a, e in zip(nombres, apellidos, edad)])   
    
    
    