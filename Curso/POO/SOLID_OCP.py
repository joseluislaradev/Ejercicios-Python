"""El pricnipio SOLID OCP(Open/Closed Principle) nos dice que las entidades de software deben estas abiertas 
para la extencion y cerradas para la modificacion, es decir, debemos de poder agregarle nuevaas funcionalidades
sin tener que modificar el codigo fuente de esa clase"""


class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    #Obligando al usuario de que cree la clase notificar en los hijos sino saldra error, tambien se puede hacer abstracta
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensajes Email a {self.usuario.email()}")
        
class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando mensajes SMS a {self.usuario.email()}")
        
#Si yo se que en un futuro se abren mas espacios para enviar notificaciones como whatsapp con esto me
# aseguro de agregar codigo y no de modificar la clase principal.
#Asi el prorama esta abierto a agregar nuevas funcionalidades siendo escalable sin modifiar la clase por
#que esta mal