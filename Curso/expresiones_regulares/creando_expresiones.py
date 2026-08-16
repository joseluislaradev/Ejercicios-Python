import re
#Detectando un numero mexicano y escondiendolo

texto = "Hola Juan, soy Jose Luis y mi numero es: +52 456-198-5911 y el otro es +54 631-118-5465"

patron = r"\+\d{2}\s\d{3}-\d{3}-\d{4}"

reemplazo = re.sub(patron, "(Numero oculto)", texto)

print(reemplazo)