# Problema: Find Pivot Index

# Dado un arreglo, devuelve el índice donde:

# suma de todos los números a la izquierda
# =
# suma de todos los números a la derecha

# El número que está en el índice no pertenece a ninguna de las dos sumas.

# Ejemplo 1
# nums = [1, 7, 3, 6, 5, 6]

# El resultado es:

# 3

# Porque en el índice 3 está el número 6:

# Izquierda: 1 + 7 + 3 = 11
# Derecha:   5 + 6     = 11
# Ejemplo 2
# nums = [1, 2, 3]

# Resultado:

# -1

# No existe ningún índice válido.

# Ejemplo 3
# nums = [2, 1, -1]

# Resultado:

# 0

# A la izquierda del índice 0 no hay números:

# Izquierda: 0
# Derecha:   1 + -1 = 0
# Firma
# def pivot_index(nums):
#     pass
# Restricciones

# Busca:

# Tiempo: O(n)
# Espacio auxiliar: O(1)

# No construyas todas las sumas de la izquierda y derecha en dos arreglos separados.



def pivot_index(nums):
    
    total_sum = sum(nums)
    left = 0
    right = 0
        
    for i, num in enumerate(nums):
        left += nums[i-1] if i-1 >= 0 else 0
        right = total_sum - left - num 
        
        if left == right:
            return i
        
    return -1
    
    
print(pivot_index([1, 7, 3, 6, 5, 6]))
# 3

print(pivot_index([1, 2, 3]))
# -1

print(pivot_index([2, 1, -1]))
# 0

print(pivot_index([]))
# -1

print(pivot_index([5]))
# 0