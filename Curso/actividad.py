productos = {
    "refresco" : 15,
    "jugo" : 12,
    "chicle" : 2, 
    "pan" : 10,
    "botana" : 8
}

total = 0

while True:
    try:
        print("*"*10,"Bienvenido :)", "*"*10)
        print("Mira el menu: \nRefresco \nJugo \nChicle \nPan \nBotana \n")
        producto = input("Ingresa el nombre del producto quieres comprar: ")
        cantidad = int(input("Cuantos quieres de ese producto? "))
        
        if(cantidad <= 0):
            print("La cantidad no puede ser menor o igual a 0")
            continue
        
        
        producto.lower()
        productoValido = producto not in productos
        
        precio = productos.get(producto)
        if(precio == None or productoValido):
            print("Por favor ingresa un producto valido")
            continue
        else:
            total += precio * cantidad
            opcion = "vacio"
            while opcion.lower() not in ('s', 'n'):
                opcion = input("\nQuieres otra cosa? (s/n): ")

                # Verifica si la opción no es 's' o 'n'
                if opcion.lower() not in ('s', 'n'):
                    print("Opción no válida. Por favor, ingrese 's' o 'n'.")
                
                # Si la opción es 'n', sal del bucle
                if opcion.lower() == 'n':
                    print("\nEl total de tu compra es: ", total)
                    print("Vuelva pronto :)")              
                    exit()
    except ValueError: 
        print("El valor ingresado en cantidad no es correcto")
