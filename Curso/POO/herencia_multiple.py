#Clase padre o super clase
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando un poco")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        #Para erencia multiple ya no usamos super() si no que hacemos referencia directa a la clase
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario= salario
        self.empresa = empresa
    
    def presentarse(self):
        return f"{super().mostrar_habilidad()}" #Con la funcion super() le decimos al programa que la funcion mostra_habilidad es un metodo heredado, es decir viene de arriba a diferencia de usar self que quiere decir que nos llamaos a nosotros mismos, ya que si tuvieramos una funcion con el mismo nombre que la clase padre, con self llamamos la actual y con super() la de la clase padre

persona1 = EmpleadoArtista("Jose Luis", 20, "Mexicana", "Guitarra", 3000, "Pepsi")

print(persona1.presentarse())


herencia = issubclass(EmpleadoArtista, Persona) #Para saber si la primera clase es subclase de la segunda, devuleve true o false
instancia = isinstance(persona1, EmpleadoArtista) #Para saber si el primer parametro es uns instancia del segundo parametro

print(instancia)