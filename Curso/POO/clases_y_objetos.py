"""Programacon orientada a objetos (POO) es una forma de programar, usada cuando la secuencial se 
queda chica ante problemas grandes y nos ayuda a hacerlos mantenibles y escalables.

Clases -> Tipos de objetos que podemos crear, definiendo todo lo que tendra nuestro objetivos como metodos o atributos que tendran todos, es como la base y apartir de ahi cambiaran despues
Objetos -> Instancia de clase, se divide en atributos y metodos
        - Atributos -> Caracteristicas de un objeto, propiedades
        - Metodos -> Acciones de un objeto, basicamente una funcion

"""

"""
class Celular():
    #Atributos estaticos (porque seeran los mismos para todos los objetos)
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"
    
celular_1 = Celular() #Creacion de un objeto(instanciar un objeto), en otras palabras crear un objeto se le llama crear una instacia de la clase Celular con los atributos de la clase. Instanciar la clase Celular para obtener la instancia de la clase celular_!

print(celular_1.marca)
"""


#Recomendacion usar Pascal Case (lo mismo que camel case pero la primera letra tambien mayuscula)
#Creacion de la clase
class Celular():
    #Atributos
    #Esto se llama metodo constructor. Cuando recien se crea un obeto es lo primero que se ejecuta
    def __init__(self, marca , modelo, camara): #Self es una manera de hacer referencia asi mismo (como acceder a las propiedades del objeto)
        self.marca = marca #self.marca es una propiedad de self y luego igualarla a marca que es el parametro que nos pasa el constructor
        self.modelo = modelo
        self.camara = camara
    
    #Metodos
    def llamar(self): #La unica diferencia con una funcion por fuera de una clase es que se le pasa el paramtreo self para poder hacer referecnia al objeto que lo crea para que uno de los parametros ea el mismo objeto que creamos
        print(f"Rin Rin. Estas llamando desde un {self.modelo}")
        
    def cortar(self):
        print(f"Upps. Cortaste la llamada desde un {self.modelo}")
        
celular_1 = Celular("Samsung", "S23", "48MP") #No se le pasa self, eso es automatico
celular_2 = Celular("Apple", "¡Phone 15 pro", "96MP") #No se le pasa self, eso es automatico. Estos se llaman atributos de instancia porque se ñlos pasamos cuando se instancia el objeto

celular_2.llamar()
    
