#Los metodos especiales son metodos resrvados con la intencion de dar funcionalidades que con
# metodos normales no podriamos, estos empiezan y termiann por dos guiones bajos

#La sobrecarga de operadores nos permite definir que pasaria si sumamos dos objetos de la misma clase o
# alguna otra opracion, , if un python todo es un objeto quiere decir que todo esta en una clase principal
#osea que hay una clase que define cada comportameinto, osea que alguien definio como se comportan las cosas
#por ejemplo al sumar un numero mas otro numero alguien defini como el "mas" se debe de comportar 


class Persona:
    #metodo contrcutor que construye el objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    #Metodo STR construye un representacion del objeto en una cadena de texto, es decir cuando se imprime el objeto en pantalla le indicamos como mostrarse.
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad = {self.edad})"
    
    #Representacion del objeto
    def __repr__(self):
        return f"Persona('{self.nombre}',{self.edad})"

    #Definiendo como se van a comportar los objetos cuando usemos el operador +
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)
        

jose = Persona("Jose", 21)
print(jose) # Aui se impirme lo que configuramos en str

repre = repr(jose) #Es lo que ingresamos en repr, la represenacion del objeto
resultado = eval(repre) #Reconstruyo el objeto

print(resultado) #Ya podria acceder a las propiedades de resultado como un objeto normal


dalto = Persona("Dalto", 30)
pedro = Persona("Pedro", 15)

nueva_persona = pedro + dalto
print(nueva_persona)
