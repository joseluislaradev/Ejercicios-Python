"""Juego de fusion


Consiste en crear los persnajes de un juego y que estos se puedan fusionar para formar personajes con mas poder.
Para ello cambiar el comportamiento del operador mas para que salgan los personajes con habiilidades mejoradas

Una posible formula es: el promedio de las habilidades de ambos al cuadrado
"""

class Personajes():
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder
    
    def __str__(self):
        return f"Persona(nombre={self.nombre}, poder={self.poder})"
        
        
    def __add__(self, otro):
        nombre_nuevo = ""
        for c1, c2 in zip(self.nombre, otro.nombre):
            nombre_nuevo += c1 + c2
        
        poder = ((self.poder + otro.poder) / 2) ** 2
        return Personajes(nombre_nuevo, poder)
    

goku = Personajes("Goku", 100)
Krilin = Personajes("Krilin", 10)
Vegueta = Personajes("Vegueta", 90)
gohan = Personajes("Gohan", 110)

fusion1 = goku + Krilin + Vegueta
print(fusion1)