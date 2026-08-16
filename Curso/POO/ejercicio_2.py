class Persona:
    def __init__(self, nombre, edad):
       self.nombre = nombre
       self.edad = edad
    
    def mostrarNombre(self):
        print(f"Tu nombre es {self.nombre} y tienes {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrarGrado(self):
        print(f"Eres estudiante de {self.grado} grado")
        
estudiante1 = Estudiante("Jose Luis", 20, 8)
estudiante1.mostrarNombre()
estudiante1.mostrarGrado()
