"""El principio SOLID ISP (Interface Segregation Principle) nos dice que el cliete no debe de estar forzado a depender
de interfaces que no utilice"""

from abc import ABC, abstractmethod


"""Esta forma puede funcionar pero esta mal puesto que robot no puede comer ni dormir y aun asi 
tenemos que definirle los metodos, este principio dice que robot no deberia estar forzad a tener interfaces
que no necesite (llamando en este contexto interfaces a las clases abstractas) ys e estaria violando
este principio"""
class Trabajador(ABC):
    
    @abstractmethod
    def trabajar():
        pass
    
    @abstractmethod
    def comer():
        pass    
    @abstractmethod
    def dormir():
        pass
    
class Humano(Trabajador):
    def trabajar():
        return "Humano chambeando"
    
    def comer():
        return "Humano comiendo"
    
    def dormir():
        return "Humano dormiendo"
    
class Robot(Trabajador):
    def trabajar():
        return "Robot chambeando"
    
    def comer():
        pass
    
    def dormir():
        pass
    
    
"""FORMA CORRECTA
Dividir la interfaz en interfaces mas pequeñas, ademas de que segun el primer principio de que las clases solo deben de hacer una funcion, 
trabajador no debe tarabajar, dormir y comer son muchas funciones"""

class Trabajador(ABC):
    @abstractmethod
    def trabajar():
        pass

class Comelon(ABC):
    @abstractmethod
    def comer():
        pass   

class Dormilon(ABC):
    @abstractmethod
    def dormir():
        pass
    
class Humano(Trabajador, Comelon, Dormilon):
    def trabajar():
        return "Humano chambeando"
    
    def comer():
        return "Humano comiendo"
    
    def dormir():
        return "Humano dormiendo"
    
    
class Robot(Trabajador):
    def trabajar():
        return "Robot chambeando"
    