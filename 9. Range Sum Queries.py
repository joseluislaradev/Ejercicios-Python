# Bloque de hoy: Range Sum Queries

# Recibes:

# Un arreglo de números.
# Varias consultas con un índice izquierdo y uno derecho.
# Por cada consulta debes devolver la suma del rango, incluyendo ambos extremos.
# nums = [3, -2, 5, 1, -4, 2]

# queries = [
#     (0, 2),
#     (2, 4),
#     (1, 5),
#     (3, 3)
# ]

# Resultados:

# (0, 2) → 3 + -2 + 5 = 6
# (2, 4) → 5 + 1 + -4 = 2
# (1, 5) → -2 + 5 + 1 + -4 + 2 = 2
# (3, 3) → 1

# Tu función debe devolver:

# [6, 2, 2, 1]
# Firma
# def range_sum_queries(nums, queries):
#     pass
# Restricción

# No debes recorrer el rango completo en cada consulta.

# La complejidad buscada es:

# Construir los prefijos: O(n)
# Resolver todas las consultas: O(q)
# Total: O(n + q)

# Donde q es la cantidad de consultas.

# Representación que debes usar

# Construye los prefijos comenzando con cero:

# nums = [3, -2, 5, 1]

# prefix = [0, 3, 1, 6, 7]

# El significado es:

# prefix[0] = suma de 0 elementos
# prefix[1] = suma de nums[0]
# prefix[2] = suma de nums[0:2]
# prefix[3] = suma de nums[0:3]

# Por eso, para una consulta inclusiva:

# left, right

# la suma es:

# prefix[right + 1] - prefix[left]

# No memorices la fórmula sin más. Piensa:

# La suma hasta después del extremo derecho menos la suma anterior al extremo izquierdo.


def range_sum_queries(nums, queries):
    
    sums = []
    actual_sum = 0
    result = []
    
    for num in nums: 
        actual_sum += num
        sums.append(actual_sum)
        
    for q in queries:
        izq_number = sums[q[0]-1] if q[0] > 0 else 0
        range_sum = sums[q[1]] - izq_number
        result.append(range_sum)
        
    return result
        
        


print(
    range_sum_queries(
        [3, -2, 5, 1, -4, 2],
        [(0, 2), (2, 4), (1, 5), (3, 3)]
    )
)
# [6, 2, 2, 1]
print(
    range_sum_queries(
        [1, 2, 3, 4],
        [(0, 3), (1, 2), (0, 0)]
    )
)
# [10, 5, 1]
print(range_sum_queries([], []))
# []





# Is o(n+k) because i am traversing two array, the first one is the numbers for get all the sums, the seconds is the queries array two get in the sums the ranges in the query array. One bucle outside other, for that reason that not is o(n*k)  
# The operation inside bucles its o(1), asign variables and keep the value in the array in the final posoition that is o(1), in the secund bucle. I access to the array with index, that is o(1) too.
# In my mind the second element oin the tuple is like that current_sum in the previous exercise, so i only need eliminate the sum previous to the start element. So I that this.
# The space complecity is o(n) because i am creating a new array with the sums of the numbers, and the result array that is the same size of the queries array. Althought, i have dudes
