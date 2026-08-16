class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")
    
    def noEstudiar(self):
        print(f"El estudiante {self.nombre} paro de estudiar")
        
nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Por favor, ingresa tu edad: "))
grado = int(input("Por favor, ingresa tu grado: "))

estudiante_1 = Estudiante(nombre, edad, grado)


while True:
    estudiar = (input("Ingresa la palabra 'estudiar' para comenzar a estudiar o cualquier otra cosa para salir: ")).lower()

    if(estudiar.lower() not in ("estudiar", "para")):
        exit()

    while estudiar.lower() in ("estudiar", "para"):
        if(estudiar == "estudiar"):
            estudiante_1.estudiar()
            estudiar = (input("Ingresa la palabra 'para' para parar de estudiar: ")).lower()
        elif(estudiar == "para"):
            estudiante_1.noEstudiar()
            estudiar = (input("Ingresa la palabra 'estudiar' para comenzar a estudiar o cualquier otra cosa para salir: : ")).lower()


    