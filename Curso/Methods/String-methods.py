#Los metodos son funciones orientadas a objetos. Todos lo metodos siempre devuelven algo
#Todos los metodos son funciones, pero no todas las fucniones son metodos, ya que los metodos son funciones especificas de objetos sino no es metodo
#lo metodo son llamados con una estructura, primero el dato, despues . y el nombre del metodo con sus parentesis
#Las funciones se llaman solo con su nombre y el datos dentro

cadena1 = "Hola,soy,Jose,Luis45"
cadena2= "estoy haciendo pruebas con Python"

mayusc = "Jose Luis".upper() #Convierte la cadena a mayusculas, es una metodo
minusc = "Jose Luis".lower() #Convierte a minusculas
primera_letra_mayusc= cadena2.capitalize() #convierte la primera letra en mayuscula, pero primero todo a minuscula y luego la primera a mayuscula

print(mayusc)
print(minusc)
print(primera_letra_mayusc)



busqueda_find = cadena1.find("Jo") #Buscamos una cadena dentro de otra y Devuelve la posicion en donde encontro lo que le pedimos ya que es un objeto, un array (devuelve -1 si no existe)
busqueda_index = cadena1.index("Hola") #Los mismo que find pero si no encuentra la cadena ocurrre un error, una excepcion 
contar_coincidencias = cadena1.count("o") #Busca una cadena dentro de otra pero cuenta cuantas veces aparece cierta cadena
contar_caracteres = len(cadena1) #Cuenta el numero de caracteres de una cadena

empieza_con = cadena1.startswith("H") #Checa si una cadena empieza con otra cadena dada, si es asi manda true sino false
termina_con = cadena1.endswith("a") #Lo mismo que start pero en el final

print(busqueda_find)
print(busqueda_index)
print(contar_coincidencias)
print(contar_caracteres)
print(empieza_con)
print(termina_con)


es_numero = cadena1.isnumeric() #Si el valor es numerico devuelve true, sino false
es_alfabetico = cadena1.isalpha() #True si tdoso los caracteres son alfabetico(letras), sino false
es_alfanumerico = cadena1.isalnum() #True si todos los caracetes son alfanumericos(letras y numeros), sino false

print(es_numero)
print(es_alfabetico)
print(es_alfanumerico)


cadena_nueva = cadena1.replace("Jose", "Pepe") #Reemplaza un pedazo de cadena por otra dada, primero va la que se reeemplazara y luego porque la reemplazaremos
cadena_separada = cadena1.split(",") #Separa cadenas con la que le pasemos y nos devuekve una lista, en este caso cada elemento separado por "," sera un elemnto
print(cadena_nueva)
print(cadena_separada)



print(dir(mayusc)) #Es uan funcion, Muestra todas los atributos o metodos que tiene el objeto que le pasamos, o lo pasamo un numero rlacionado con eo, un tring pue con eo



