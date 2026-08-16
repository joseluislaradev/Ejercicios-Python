# Manejar la complejidad ocultadnole todo lo innecesario al programador y al usuario y dandole solo
# las funcionalidades relvantes, En pocas palabras, darle una interfaz simple que oculte una compleja
# el encapsulamiento era una forma de trabajr con abstraccion porque eran metodos privados que solo con 
# el objeto.nombre la funcion podiamos hacer editar, recibir o eliminar un archivo cuando por dentro la 
# complidad es mayor porque estamos usand decoradores, setter, getters, del, ocultamos lo complejo y lo 
# dejamos simple porque no necesitamos sabr como funciona internamente sino solo como usarlo.
# como cuando usamos un celualr, no necesitamos saber como fucniona internamente pero sabemos que si presionamos un boton prende


class Auto():
    def __init__(self):
        self.estado = "apagado"

    def encender(self):
        self.estado = "encendido"
        print("El auto esta encendido")

    def conducir(self):
        if self.estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
mi_auto = Auto()
mi_auto.conducir() #Aqui ya hay abstraccion, al usuario le doy la funcion condicir pero el no sabe toda la logica detras

            



