# Una clase abstracta es una clase que no podemos instanciar, 
# es una plantilla para crear clases apartir de ella
#Es como si fura herencia pero mas complejo, la diferencia es que la clase padre solo seria como
#la plantilla base pero no podriamos crear un objeto de ella en si como si sucede en herencia

#Implementar un metodo, es definir como va a funcionar, es decir su contenido

#Un metodo abstarcto es un metodo dentro de una clase abstracta sin implementacion, normalmente se hace para que cuando se cree otra clase que herede de la abstracta poder implmentar el metodo

from abc import ABC, abstractmethod #abstractmethod es un decorador que permite indicar a la clase que estamos usadno un metodo abstracto

class Persona(ABC): #Herando de ABC hacemos que sea una clase abstracta
    @abstractmethod #Con este decorados indicamos que crearemos un meotod abstracto
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre        
        self.edad = edad        
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractmethod
    def hacer_actividad(self): #La creamos porque el contenido de como trabaja un persona, lo que hace en su trabajo puede ser diferntge
        pass        

    def presentarse(self):
        print(f"Hola me llamo: {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Estoy trabajando en el rubro de: {self.actividad}")

#Nota: En la clase hija se debe obligatoriamente implementar los metodos abstractos de la clase padre pàra que se puede instanciar una clase
jose = Estudiante("Jose", 20, "Masculino", "Programacion") 
dalto = Trabajador("Dalto", 30, "Moviliario", "Programacion") 

jose.presentarse()
jose.hacer_actividad()

dalto.presentarse()
dalto.hacer_actividad()


#La razon por la que se crean clase abstractas y no solo herdamos como tal, que en muchos casos se hace asi
#es por asi nos obligamos que las clases que hereden de la abstracta tengan los metodos que definimos como
#abstractos implmentados porqe sino no funcionara, ademas fomenta el polimorfismo ya que todas las clases 
#estan obligadas a tener los mismos metodos y por eso pueden ser usados por todas las subclases
