#Creando una funcion que nos devuelva los numeros primos entre 0 y el argumento que pasemos

num = int(input("Ingresa hasta que numero quieres saber los numeros primos: "))

#Nos dice especificamente si un numero es primo, viendo todos los elementos por los que se puede dividir
def es_primo(num):
    #NOTA: La funcion range tiene otro parametro qeu es la cantidad de saltos que da
    for i in range(2,num): #Va desde 2 porque uno no es numero primo, y hasta num para no dividir el valor por si mismo, ya que el valor de num no entra e la cuenta de range
        if num%i==0: return False #Si hay otro numero que al dividirlo su residuo sea 0 quiere decir que no es primo, es compuestp
    return True #Si no se pudo diviidir por otro numero, es primo.

#Nos dice todos lo numeros primos hasta llegar a un numero
def primos_hasta(num):
    primos = []
    for i in range(2,num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta(num)
print(resultado)
