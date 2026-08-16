print("*"*10,"Programa del Jose Luis ausente", "*"*10)
lado = []

def area():
    f = sum(lado) / 2
    area = (f * ((f-lado[0]) * (f-lado[1]) * (f-lado[2]))) ** .5
    return area

def podercontruir():
    prueba1 = (lado[0] + lado[1]) > lado[2]
    prueba2 = (lado[0] + lado[2]) > lado[1]
    prueba3 = (lado[1] + lado[2]) > lado[0]

    if(prueba1 and prueba2 and prueba3):
        print("Puede construirse")
        print("El area es: ", area())
    else:
        print("No puede construirse")
       

for i in range(3):
    lado1 = int(input(f"Ingresa la medida del lado {i+1}: "))
    lado.append(lado1)
    
    
podercontruir()
