"""El encapsulamiento consiste en proteger lso elemntos de una clase (metodos o variables)

Como que un desarrollador vea las propiedades constraseña de la clase facebook

El encapsulamiento lo que hace es ocultar una complejidad interna de las clase y proteger los atributos cuand se poenen como privados obligando
a que para acceder a los datos dse haga de otra forma"""

class MiClase:
    def __init__(self):
        #La manera de hacerlo privado es con un guion bajo despues del punto, pero el desarrollador puede seguir accediendo al valor aunque el entiende que no deberia
        self._atributo_privado = "Hola"
        #Con dos guones bajos despues del punto indicamos que es muiy muy proivado y de verdad no podemos acceder al valor (tira error, auqnue en realidad si hay una forma de acceder)
        self.__atributo_muy_privado = "Soy bien privado" 
        
    def __hablar(self): #Metodo privado
        print("Hola como estas")

objeto = MiClase()
print(objeto._atributo_privado) 
#print(objeto.__atributo_muy_privado)
#print(objeto.__hablar())