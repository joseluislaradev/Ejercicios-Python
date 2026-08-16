print("*"*10,"Programa para saber los numeros primos en un rango dado", "*"*10, "\n")

numeros_primos=[] #Guardara los numeros primos detectados en el rango

#Comprueba que un solo numero sea primo
def es_primo(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

#Recorre todos los numeros en el rango y verifica todos para ver cual es o no primo
def numeros(inf, sup):
    if(inf < 2):
        inf = 2
        
    for num in range(inf,sup+1):
        retorno = es_primo(num)
        if retorno == True:
            numeros_primos.append(num)

#Comprobaciones de seguridad al ingresar datos.
def comprobaciones(inf,sup):
    if inf > sup:
        print("Error: El numero superior no puede ser menor que el inferior.")
        return False
    if inf < 0 or sup < 0:
        print("Error: No puede haber numeros negativos.")
        return False
    return True

#Ejecucion completa, pedida de datos y llamdaa a las otras funcines
def ejecucionPrograma(): 
    inf = 0
    sup = 0
    
    try: 
        # Solicitar al usuario que ingrese un número entero
        inf= int(input("Rango inferior: "))
        sup= int(input("Rango superior: "))
        
        comprobacion = comprobaciones(inf,sup)

        if comprobacion == True:
            numeros(inf,sup)
            #Mostrando: numeros primos
            print("Los numeros primos en el rango", inf, "-", sup ," son: ")
            for i in numeros_primos:
                print(i)
 
    except ValueError:
        # Si ocurre un ValueError (cuando no se puede convertir a entero), mostrar un mensaje de error
        print("Error: Debe ingresar un número entero.")


while True:

    ejecucionPrograma()
    
    #Cuando ya se ejecuto una vez y termino por alguna razon preguntar para ejecutarlo de nuevo
    print()
    
    opcion = "vacio"
    while opcion.lower() not in ('s', 'n'):
        opcion = input("¿Desea continuar? (s/n): ")

        # Verifica si la opción no es 's' o 'n'
        if opcion.lower() not in ('s', 'n'):
            print("Opción no válida. Por favor, ingrese 's' o 'n'.")
        
        # Si la opción es 'n', sal del bucle
        if opcion.lower() == 'n':
            exit() 
        

    




    
            
        

    
        



    
    
