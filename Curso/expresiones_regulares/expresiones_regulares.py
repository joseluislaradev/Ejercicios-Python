import re

texto = """Hola maestro. esta es la cadena 1, como estas mi capitan
Esta es la abababablinea 265 del ababbabbbbbbaatexto
Y esta es la ultima final definitiva mi capitan"""

#Haciendo una buscqueda simple
resultado = re.search("Hola", texto) #Primero la cadena a buscar, despues en donde, devuelve un objeto match donde los encontro solo el primero
resultado = re.findall("esta", texto, flags=re.IGNORECASE) #devuelve lista con todas las apariciciones, opcional un tercer parametro para añadir funcion adicional como flags=re.IGNORECASE (ignora mayusculas o minusculas)

#\d -> busca los digitos numericos del 0 al 9
resultado = re.findall(r"\d", texto) #Se pone una r para indicar que se incluiran expresiones regulares en la cadena

#\D -> busca TODO MENOS numericos del 0 al 9
resultado = re.findall(r"\D", texto) 

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _] En pyhton el guion bajo se considera alfanumerico
resultado = re.findall(r"\w", texto) 

#\W -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _] En pyhton el guion bajo se considera alfanumerico
resultado = re.findall(r"\W", texto) 

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\s", texto) 

#\S -> busca TODOS MENOS LOS espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\S", texto) 

#. -> busca TODOS MENOS saltos de linea
resultado = re.findall(r".", texto) 

#\n -> busca saltos de linea
resultado = re.findall(r"\n", texto) 

#\ -> cancela caracteres especiales,es decir todo lo que no es alfanumerico (numeros y letras)
resultado = re.findall(r"\.", texto) #La fuccionalidad que tienen por defecto el punto solo ahora no la tiene y solo buscara el punto

#Armando una cadena que bsque un numero, seguido de un punto y un espacio
resultado = re.findall(r"\d,\s", texto)

#^ -> Busca el comienza de una linea 
resultado = re.findall(r"^Hola", texto, flags=re.M) #Busca si la palabra Hola esta al principo de una linea, si no podemos el flags = re.M solo se fija en la primera linea(porque considera todo el texto como una sola linea), con la m le decimos que sea multilinea y que despues de cada \n lo considera una nueva linea

#$ -> Busca el final de una linea 
resultado = re.findall(r"capitan$", texto, flags=re.M)

#* -> Afecta al anterior operador encontrando cero o mas ocurrencias
resultado = re.findall(r"Hola.*", texto) #Busca hola seguido de algo que no sea un salto de linea, el signo * indica que devolvera todo lo que no sea salto de linea o si no hay nada tambien es valido

#* -> Afecta al anterior operador encontrando una o mas ocurrencias
resultado = re.findall(r"Hola.*", texto) #Busca hola seguido de algo que no sea un salto de linea, el signo * indica que devolvera todo lo que no sea salto de linea pero a diferencia de el * debe de haber una o mas coincidienias

#{n} -> Busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r"\d{3}", texto) #La primera parte (\d) le decimos que busque un numero y luego le indicamos con {3} que busque 3 veces esos, osea 3 numeros juntos

#{n,m} -> el menos n, maximo m
resultado = re.findall(r"\d{1,4}", texto) #Devuelve todos los valores donde encuentra como minimo un numero y como maximo 4 numeros juntos (si un numero es eneorme como 4574784, tomara los primeros 4 y los mandara en un elemento de la lista y los que sobran los mandara en otor elemnto y asi )

#{n,m} -> el menos n, maximo m
resultado = re.findall(r"ab{1,4}", texto) #Busca una sola "a" que despues tenga entre 1 y cuatro "b", para que se enceuntre la a y la b en conjunto al menos 1 a 4 veces se encierra entre aprentesis (ab){1,4} 

resultado = re.findall(r"(ab){2}", texto) #Si solo se pone un argumento, devolvera un elemnto de la lista cuando encuentre 2 veces la cadae de la izquierda es decir, solo si encuentra abab, es como si el numero lo multiplciacra (no devuelve abab devuelve ab, una cosa es lo que buscamos y otra lo que devuelve, es como que le decimos que busque ababa pero devuleva ab)

resultado = re.findall(r"[ab]{2}", texto) #Nos decuelve la combinacion, intenta encontrar 2 veces cada elemento de la izquiera, que coincida el primer elemento con a y b y eso dos veces

"""
[ab]: Coincide con cualquier carácter 'a' o 'b'.
[123]: Coincide con cualquier dígito '1', '2' o '3'.
[a-z]: Coincide con cualquier letra minúscula del alfabeto inglés.
[0-9]: Coincide con cualquier dígito del 0 al 9.

El cuantificador {2} que sigue al conjunto de corchetes indica que se espera que 
la secuencia contenida dentro de los corchetes se repita exactamente dos veces
"""

# | -> Busca una cosa o la otra (en realidad deveulve las dos, si encuentra 1 la devuelve y si encuentra la otra tambein)
resultado = re.findall(r"\d{2}|Hola", texto) #Devuelve primero Hola en la lista  porque en la cadena sale primero que en los numeros

print(resultado)
