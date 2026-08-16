#Creando una funcion simple
def saludar():
    print("Hola Jose luis, ¿Que haces?")
    
#Ejecutando la funcion simple
saludar()

#Creando una funcion con parametros(variable que existe dentro de una funcion y afuera no)
def saludar2(nombre, sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "amor"
    
    print(f"Hola {nombre}, mi {adjetivo} ¿como estas?")


saludar2("Juan", "HomBrE")
saludar2("Pedro", "Mobiliario")
saludar2("Marco", "Caballo")


#Creando una funcion que retorne valores

def crear_contraseña_random(num):
    chars = "abcdefghij"
    numero_a_cadena = str(num)
    numero_entero = int(numero_a_cadena[0])
    c1 = numero_entero - 2
    c2 = numero_entero 
    c3 = numero_entero - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña #Paodemos devolver una tupla sin necesidad de ponerla entre parentesis

password = crear_contraseña_random(78)
print(f"Tu contraseña nueva es: {password}")