"""SOLID es una estilo de programacion que nos permite crear codigo de calidad, es decir facil de entender, 
estructurado, escalable, reutilizable, etc. SOLID fue creado en su momento para lenguajes de tipado estatitco pero 
en realidad tambien son aplicables al tipado dinamico y no seguirlos es una mala practica de programacion.

SRP (Single Responsability Principle) - Una clase debe tener una unica responsabilidad o tarea,como una persona en un 
trabajo que solo hace una cosa como un progrmaador que solo programa, si se haen mas de dos separar en clases
Esto para que las clases esten mas limpias y faciles de mantener, tambien hace que la clase haga lo suyo sin depender de
otras clases.

"""

#En este clase tenemos una de auto que se encarga del movimeinto, pero tambien del combustible y no debe de encargarse de todo segun SOLID
"""
class Auto():
    def __init__(self):
        self.posicion = 0
        self.combustible = 100
        
    def mover(self, distancia):
        if self.combustible >= distancia / 2:
            self.posicion += distancia
            self.combustible -= distancia / 2
        else:
            print("No hay suficiente combustible")
            
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustibel(self):
        return self.combustible
"""

class TanqueDeCombustible():
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia /2)
            print("Haz movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")
            
    def obtener_posicion(self):
        return self.posicion
        

tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtener_posicion())
autito.mover(10)
print(autito.obtener_posicion())
autito.mover(20)
print(autito.obtener_posicion())
autito.mover(60)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())
