nombre = True

#Al póner nombres a las cosas, al separar parabras si usamos una letra mayuscula se llama "camel-case" si se usa
#guiion bajo se llama "snake-case"

#Concatenar con f-strings, pone el valor que esta dentro de la variable como texto
bienvenida = f"Hola {nombre} ¿Como estas?"
bienvenida = f"Hola {nombre:_<10} ¿Como estas?" #^

#del bienvenida - Este operador elimina una vairable declarada
print(bienvenida)

#concatenar con mas
nombre="Jose Luis"
bienvenida = "Hola " + nombre + " ¿Como estas?"
print(bienvenida)

 #Busca ola dentro de la variable bienvenida y responde true o false. se puede poner not in
 #estos son operadores de pertenencia (in / not in)
print("ola" not in bienvenida) 




