class Animal:
    def comer(self):
        print("Estas comiendo")
        
class Mamifero(Animal):
    def amamantar(self):
        print("Estas amamantando")
        
class Ave(Animal):
    def volar(self):
        print("Estas volando")
        
class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()
