"""
Un modulo son todas los archivos con la extension .py llamados asi puesto que desde un modulo 
podemos llamar, crear, cambias rutas, formar paquetes, etc.
Hya tres los python modules que son:
    - Los que ya trae python peero estan escrtos en C
    - Los modulos de terceros"dear party module" son los que creo alguien mas, regularmente subidos en internet
    y los decargamos
    - Los own modules que son los creados nosotros mismos.
"""

import modulo_saludar #Se importa todas las funciones del modulo_saludar para poderla utilizar aqui, lo cual es llamado namespace conjunto de todos los metodos y cosas dentro de ese modulo
import modulo_saludar as modulo #Nos permite darle un nombre corto al namespace

saludo = modulo_saludar.saludar("Jose Luis") #El archvio agregado se comporta con un objeto el cual tiene sus funciones
print(saludo)

print(type(modulo_saludar)) #El tipo es module porque es un modulo,


from modulo_saludar import saludar,saludar_raro #Importando dos funciones solo, tambien funciona el as
from modulo_saludar import * #Importa todas las funciones, la unica diferencia con import seria la forma en que se llaman, pero es mala practica porque el programa se hace muy pesado innecesariamente si no se utiliza todo si el modulo es grande

#Si tiene menos jerarquia el modulo (esta dentro de una capeta en la misma ruta)
#import modulo_saludar.carpeta.saludar 

#Para mas jerarquia (retroceder en la ruta)
import sys #sys es un modulo de python (built-in)

sys.path.append("C:\\xampp\\htdocs\\python curso\\.vscode\\funciones_buenas_modulo") #Se agrega la ruta a la cual no se tiene acceso

print(sys.builtin_module_names) #devuelve una t modulos que estan en sys (estan creados en c), parecido a dir. No crear modulos con el mismo nombre que estos porque python le da prioridad a estos
print(sys.path) #Devuelve todas las rutas de los modulos que estan en sys

#import saludar "Para importar con sys se pone el nombre la funcion"
#print(saludar.saludar("Jose Luis 2"))


"""Tambien se pueden importar vairbales especificas, si tienen el mismo nombre que las funciones es un problema
si las ponemos antes de las funciones no se ejecuta nada y si las ponemos despues de la funcion pero tiene el
mismo nombre la vairable y despues qeuremos usar la funcion importada no lo tomara como funcion porque lo tomara
con el valor de la variable. 
Para esto hay metodologias como escribir la primera letra de las funciones en mayusculas y las viarbales en
minuscualas para que se confundan los nombres"""

print(saludar("Juan")) #Ahora si actuan como funciones normales
print(saludar_raro("Pedro"))

#accedemos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado
print(modulo_saludar.__name__)

print(dir(modulo_saludar))