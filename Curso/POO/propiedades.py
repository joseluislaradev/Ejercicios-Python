# Las propiedades son getters, setter y delete

class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property #Es un decorador especial que declara la sigueinte fucnion como un getter
    def nombre(self): #Esto es un getter, un getter es una funcion que accede a un atriuto privado o muy privado
        return self.__nombre
    
    @nombre.setter #Decorador que permite hacer un setter a la funcion tamien
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
        
    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
dalto = Persona("Lucas", 21)

nombre = dalto.nombre #No pongo los parentesis de la funcion ya que estoy usando el decorados property
print(nombre)

dalto.nombre = "Pepe"

#del dalto.nombre

nombre = dalto.nombre

print(nombre)



