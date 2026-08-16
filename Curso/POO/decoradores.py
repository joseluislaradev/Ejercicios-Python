"""Un decorador toma una funcion, le agrega una cosas extra y regresa el resultado 
de la fucnion mas las cosas extra que agrego"""

def decorador(funcion):
    def funcion_modificadora():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    
    return funcion_modificadora


# def saludo():
#     print("hola dalto")

# saludo_modificado = decorador(saludo) #Convertimos una variable a una fucnion
# saludo_modificado()

@decorador
def saludo():
    print("Hola dalto como pijas estas")
    
saludo()