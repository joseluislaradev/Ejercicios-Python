def sumar_dos(): 
    while True:
        try:
            a = int(input("Numero 1: "))
            b = int(input("Numero 2: "))
            resultado = a + b
        except Exception as e:
            print("Te pedi un numero, pon uno")
            print(f"NombreError: {type(e).__name__}")
            print(f"Error: {e}")
        else: #El else en una excepcion se ejecuta si no se ejecuto el except, es decir, se ejcuta cuando no salio errores
            break
        finally: #Se ejecuta siempre, sin importar si se encontro o no una ecxepcion o se ejcuto el else
            print("Esto se ejecuta siempre")
        

    return resultado

print(sumar_dos())