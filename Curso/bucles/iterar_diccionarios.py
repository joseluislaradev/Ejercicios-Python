diccionario = {
    "nombre": "Jose Luis",
    "apellido": "lara",
    "canal": "MasteLuis"
}

#Recorriendo diccionario para obtner las claves
for key in diccionario:
    print(key)
    
#Recorriendo diccionario con items() para obtner las claves y el valor, devuelve una tupla, al igual que enumerate en listas
for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f"La calve es {key} y el valor es {valor}")
    