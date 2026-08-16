"""El principio SOLID LSP (Liskov's Substitution Principle) establece que las clases derivadas tienen que 
poder ser sustituibles por las clases base, es decir, si la clase B es una subclase de A, la clase B debe poder
hacer todo lo que haga A, es decir la clase padre, el fin es hacer el codigo mas legible"""


"""Problmea de esta forma es que Pinguino es una subclase de Ave y deberia poder volar, pero no puede, aqui se rompe
el principio SOLID puesto que la clase hija no puede hacer todo loq ue haga la padre. 
despues si queremos que la clase Ave haga lo mismo que la de pinguino no se podra, porque tenemos que las
aves si vuelan y en pinguino no, la solucion es dividir las clases en mas categorias en donde la clase Ave 
tenga solo o que si tgienen en comun otras aves, volar no aplica porque como vimos hay unas que no vuelan, o
hay otras que nadan"""
class Ave:
    def volar(self):
        return "Estoy volando"
    
class Pinguino(Ave):
    def volar(self):
        return "No puedo volar :("
    
def hacer_volar(ave = Ave):
    return ave.volar

print(hacer_volar(Pinguino()))




#forma de hacerlo aplicando el principio

class Ave:
    pass #Aqui ponemos todo loq ue si tengan en comun las aves

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    
class AveNoVoladora(Ave): #Asi todos los que hereden de la calse basedeben poder hacer lo que la clase base haga
    def volar(self):
        return "No puedo volar"


