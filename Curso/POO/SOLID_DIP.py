"""El principio SOLID DIP (Dependency Inversion Principle) establece que los modulos de alto nivel no deben
depender de los de bajo nivel, los dos deben de depender de las abstracciones, a su ves las abstracciones no
deben depender de los detalles sino los detalles de las abstracciones.
Mas simple es, el codigo no debe depender de implenmentaciones espcificas como funciones o codigo sque hagan
algo si no de interfaces mas complejas, asi las de clases de mas alto nivel con toda la logica se mantiene independientes
de la de bajo nivel que hacen fucniones especificas, esto permite cambiar cosas abajo sin afectar arriba"""


#Aqui tneemos el problema de que la funcion  corregir texto del CorrectorOrtografico, depende mcuho de la clase
#diccionario la cual tiene todas las funciones  para verificar si es correcta y son usadas por las funcuin
#corregir texto, el problema es que la clase CorrectorOrtografico es mucho mas importante que la de diccionario
#y no deberia depender de ella, porque si editamos la clase mas chica osea Diccionario estariamos afectando 
#la clase mas grande lo cual no tiene sentido, deberia ser al reves
class Diccionario:
    def verificar_palabras(self, palabra):
        #Logica para verificar palabras
        pass
 
class CorrectorOrtografico:
    def __init__(self, diccionario):
        self.diccionario = Diccionario()
        
    def corregir_texto(self, texto):
        #Usamos el diccionario para corregir texto 
        pass
     
    
#Solucion, aqui dependemos de una interfaz es decir de la abatraccion de metodo verificar palabras, que puede
# haber muchas clases que hereden de ahi y se vean obligadas a tener todas las funciones que tienen la clase padre
# y la calse corrector ortografico ya no depende directamente de la implenmntacion de una, si no de la abstraccion
# asi que puede usar la que quiera

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras si esta en el diccionario
        pass
    
class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras si esta en el diccionario
        pass
    
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        #Usamos el verificador para corregir texto 
        pass

corrector = CorrectorOrtografico(Diccionario())
corrector2 = CorrectorOrtografico(ServicioOnline())