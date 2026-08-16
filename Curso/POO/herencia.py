"""
La herencia permite a la clase hija acceder a los metodos y atributos de la clase padre.
La clase padre podria ser galleta y los atirbutos y metodos de una galleta normal, luego
las clases hijas tienen lo mismo de la calse pade pero agregan cositas que la hacen diferente como
unas chispas de chocolate, otra tal vez mas harina, etc.

Existen varios tipos de herencia: 
Simple - Una sola clase padre y una hijo
Jerarquica - Hay muchas clases hijo que dependen de solo una clase padre
Multiple - Una clase hija que hereda de dos clases

"""


#Clase padre o super clase
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando un poco")


#Clase hija o subclase
class Empleado(Persona):
    #Forma de heredar atributos ya gregar los propios
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario): #Indicamos todos los atributos, los que heraedamos y los nuevos
        super().__init__(nombre, edad, nacionalidad) #Indicamos los atributos que vamos a heredar
        #Definimos el valor de los nuevos atributos
        self.trabajo = trabajo
        self.salario = salario

    #Si agregamos un metodo con el mismo nombre que la clase padre(SUPERCLASE) se sorbrescribe, si no lo ponemos sale el mismo
    def hablar(self):
        print("SOBREESCRITO")
        
    #pass #Nos ayuda a definir algo que no hara nada pero para que no tire error por dejarlo vacio

roberto= Empleado("Roberto", 43, "argentino", "Carpintero", 1800)

print(roberto.trabajo)
roberto.hablar()