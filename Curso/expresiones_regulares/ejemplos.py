import re

#Para reemplazar
text = "Reemplazando todas las vocales por asteriscos"
new_text = re.sub(r"[aeiou]", "*", text ) #Primero es el patron, luego por lo que se reempelzara y despues el texto en el que lo hra
print(new_text)

#Para verificar
def validar_correo(correo):
    # Patrón de expresión regular para validar un correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Intenta hacer coincidir el patrón con la dirección de correo
    if re.match(patron, correo):
        return True
    else:
        return False

# Ejemplo de uso
direccion_correo = "usuario@example.com"
if validar_correo(direccion_correo):
    print("La dirección de correo es válida.")
else:
    print("La dirección de correo no es válida.")
    

#Encontrar paginas web del texto
import re

def encontrar_urls(texto):
    # Patrón de expresión regular para encontrar URLs
    patron = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' #Otra fomra: https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+
    
    # Encontrar todas las coincidencias en el texto
    urls_encontradas = re.findall(patron, texto)
    return urls_encontradas

# Ejemplo de uso 
texto_ejemplo = "Aquí hay una URL de ejemplo: https://www.ejemplo.com y otra más: http://otraejemplo.com"
urls = encontrar_urls(texto_ejemplo)
print("URLs encontradas:", urls)