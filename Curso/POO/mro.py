"""
MRO (METHOD RESOLUTION ORDER) el metodos de resolucion de orden hace referencia al orden en que 
python busca metodos y atributos en las clases, por ejemplo si tenemos muchas herencias con el mismo
nombre en un metodo cual tomara primero y despues algo.
"""

class A:
    def hablar(self):
        print("Hola desde A")
        
class F(A):
    def hablar(self):
        print("Hola desde F")
        
class B(A):
    def hablar(self):
        print("Hola desde B")

class C(F):
    def hablar(self):
        print("Hola desde C")
            
class E(F):
    def hablar(self):
        print("Hola desde E")
       
class D(B, C, E):
    def hablar(self):
        print("Hola desde D")
        
d = D()

d.hablar()

print(D.mro())

#El MRO nos dice el orden pero para poder ejecutar la funcion de alguna clase en espcifico 
F.hablar(d) #La clase superior que queremos llamar, la fucnion de esa clase y el objeto de la clase inferior