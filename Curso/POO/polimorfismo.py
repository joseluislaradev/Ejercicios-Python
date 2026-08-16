"""
El polimorismo(poli viene de muchos y morfismo que viene de morfos que significa forma) hace referencia a 
enviarle un mensaje sintactico a varios objetos pero el mensaje es el mismo
pero el resultado diferente, Si yo envio un mensaje que diga "haz lo tuyo", el objeto perro ladrara, gato
mauya, la vaca hace muu, etc. diferentes resultados porque son distintos obejtos con
distintas propiedades pero con el mismo mensaje.

Polimorfismo en tiempo de ejecucion o de inclusion, esto es como las varibales, es una sola variable pero
puede ser de muchos tipos, la llamamos a pantalla con el mismo nombre pero sea del tip que sea lo imprimira
en pantalla sea un objeto, texto, et.

"""
class Animal():
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "miau"

class Perro(Animal):
    def sonido(self):
        return "Gua"

def hacer_sonido(animal):
        print(animal.sonido())
    

gato = Gato() #Hay dos conceptos aqui, el tipo de varibale decalrado, en este caso es gato, pero el tipo real en este caso es Animal puesto que es la clase base
perro = Perro()

#Los enlaces dinamicos es un mecanicsmo interno para saber que metodo usar en un objeto cuando lo llamamos, al del hijo o al del padre, esto dependiendo si el lenguaje es dinamico o estatico

print(perro.sonido()) #Polimorfismo de inclusion o add-op porque solo con la palbra sonido() puedo hacer diferentes cosas con solo cambiar el objeto

hacer_sonido(gato) #polimorfismo de funcion, misma funcion pero cambia el argumento

#polimorfismo de herencia tambien llamado de subtipos o subclase
"""Solo esta en otros lenguajes de tipado estatico donde no se pueden tener un funcion con el mismo nombre
auqneu sea en diferentes clases, afuerzas tiene que heredarlos y ya de ahi ahora si pueden redefinirlos.
Como este lenguaje es de tipado dinamico no necesitamos que herede de otras y podemos poner la misma funcion
end diferentes clases, no importa de donde sea o de donde provenga si tiene la funcion la clase ahi es"""

#Polimorfismo de sobrecarga
"""No existe en python pero en java por ejemplo, es una clase con un monton de funciones del mismo nombre
pero que piden parametros diferentes, entonces segun los parametros que le pasemos la clase se comportara
diferente entrando a alguna de las funciones"""

#Polimorfismo de coercion
num1 = 3
num2 = 4.4

resultado = num1 + num2 #El entero lo convierte a flotante para sumarlo, sin importar el tipo que sea
# la implementacion es la misma pero se adapata al tipo de dato que sea, por eso hay polimorfismo
# es decirm misma funcion, diferente dato y funciona igual

print(resultado)

