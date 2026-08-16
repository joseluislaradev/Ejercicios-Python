class Persona():
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self.__edad = edad
    
    def get_nombre(self): #Esto es un getter, un getter es una funcion que accede a un atriuto privado o muy privado
        return self._nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, nuevo_nombre): #Esto es un letter, una funcion que permite actualizar el atributo privado
        self._nombre = nuevo_nombre

dalto = Persona("Lucas", 21)
print(dalto._nombre) #Como el atributo tiene un guion bajo, no debemos acceder de esta forma, auqnue se pueda

nombre = dalto.get_nombre()
print(nombre)

edad = dalto.get_edad()
print(edad)

dalto.set_nombre("Juan")

nombre = dalto.get_nombre()
print(nombre)


