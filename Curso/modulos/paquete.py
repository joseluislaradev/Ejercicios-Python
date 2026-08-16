#Un paquete es una carpeta con muchos modulos (archivos python) 
#Un modulo normalmente busca hacer una accion especifica y cuando tenemos un porgrama completo bien hecho s tenemos muchos modulos
#En lugar de importar cada modulo uno por 1 importamos todos el paquete.

#Para eso agregmos un archivo al paquete llamado __init__.py es un archivo que cuando pthon lo ve entiende que es un packete y no un modulo

#Si tenemos un archivo o una carpeta con el mismo nombre siempre le da prioridad a la carpeta
import paquetes.saludar #Aqui ya importo todo el paquete, ya esta agregado a la ruta por tanto ya estan todos los archivos

print(type(paquetes))
print(paquetes.saludar.saludar("Jose")) #Primero la carpeta, luego el archivo y por ultimo la funcion

 