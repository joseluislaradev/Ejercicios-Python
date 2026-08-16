planetas = []

planetas.append("Venus")
planetas.append("tierra")
planetas.append("jupiter")
planetas.append("saturno")

for i in range(3):
    usuario = input("Porfavor ingresa los planetas Urano, neptuno y pluton en orden")
    planetas.append(usuario)

planetas.insert(2, "Marte")

del planetas[-1]

planetas.insert(0, "Mercurio")

print(planetas)