#Creando un conjunto con set
conjunto = set(["dato1", "dato2", ("dato3", "dato4")]) #Los conjunto son inmutables por lo tanto no pueden tener una lista o diccionaio dentro ya que estos si lo son, pero una tupla si ya no se modifica

#Metiendo un conjunto dentro de otro conjunto
conjunto0 = {"dato1", "dato2"} #Conjunto normal no se puede meter dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"]) #FrozenSet crea un conjunto inmutable pero congelado como que sea hashseabley ya no pueda cambiar su valor interno ys e puede meter dentro de un conjunto
conjunto2 = {conjunto1, "dato3"}

print(conjunto)
print(conjunto2)

#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}

resultado = conjunto2.issubset(conjunto1)#Para ver si un conjunto es un subconjunto de otro, devuelve true o false
resultado = conjunto2 <= conjunto1 # Porque conjunto 2 tiene que ser menor o igual en elementos que conjunto 1 para ser subconnjunto, ya la comparacion de que si sean los numeros que tiene que ser se hace implicitamente
print(resultado)

resultado = conjunto2.issuperset(conjunto1)#Para ver si un conjunto es superconjunto de otro, devuelve tru o false
resultado = conjunto2 > conjunto1 #Porque conjunto 2 tiene que ser mayor ene elemntos que conjunto 1 para ser superconjunto, ya la comparacion de que sean los mimos mas otros se hace implicitamnete
print(resultado)

#Verificar si no hay algun numero en comun entre dos conjuntos
resultado = conjunto2.isdisjoint(conjunto1) #Si hay un numero elemento en el conjunto1 que este en el conjunto2 devulve false, si no hay ninguno en comun devuelve true
print(resultado)