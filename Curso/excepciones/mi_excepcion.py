#Creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")


#Lanzando mi propia excepcion
#raise MiExcepcion("Este es un error que yo cree") #Raise manda a llamar a una excepcion, no solo nuestra, por ejemplo raise ValueError


#Manejando mi propia excepcion
try:
    raise MiExcepcion("Este es un error que yo cree") #Raise manda a llamar a una excepcion, no solo nuestra, por ejemplo raise ValueError
except:
    print("Como cometiste ese error mi progamador de elite")