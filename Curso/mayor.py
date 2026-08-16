print("Programa para saber que numero e el mayor de 3")
print("Ingresa tres numeros")
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo nuemro: "))
num3 = float(input("Ingresa el tercer nuemro: "))

numMayor = max(num1, num2, num3)
numMenor = min(num1, num2, num3)

print("El numero mayor es: ",  numMayor)
print("El numero menor es: ", numMenor)