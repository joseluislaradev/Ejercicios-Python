#Creando tupla con tuple
tupla = tuple(["dato2", "dato2"])

#Creando tupla sin parentesis de solo un dato
tupla = "dato1",

#Creando tupla sin parentesis
tupla = "dato1", "dato2" #Aqui tambine se creo una tupla, e vez de desempaquetar se podria decir que se empaqueta

#Las tuplas son utiles cuando los datos son de solo lectura, puesto que se puede optimizar el usao de memoria ya que no cambiaran
#Las lista necesitan mas memoria que las tuplas y pyton intenta adivinar cuanto crecera ocupando mas memoria, si se supero se pueden llegar a cosas como fragmentar la informacion    

#Las listas al ser mutables necesitan guardar mas info que ayuden a expandirla el tamaño y contenido cuando sea necesario, tal vez como el tamaño actual, o la capacidad total, las tuplas son ams eficeintes en memoria porque guardan los datos en un unico bloque de memoria no necesita mas info ya que no se modificara.

#Los conjunto pueden ayudar a reducir el usao de memoria ya que evita duplicados
#Los diccionarios funcionan con tablas hash para acceder rapidamente, se puede llegar a requerir memoria para gestionar colisiones pero la desventaja se ve superada por su eficiencia en busqueda
#lo dicccionario no son lista, almacenan valores ne clave -valor, las listas son numericos consecutivos

print(tupla)