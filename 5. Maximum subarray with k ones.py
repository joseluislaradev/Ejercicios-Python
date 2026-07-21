# Problema: máximo subarreglo con hasta k ceros

# Recibes un arreglo binario nums, compuesto únicamente por 0 y 1, y un entero k.

# Puedes cambiar como máximo k ceros por unos. Devuelve la longitud máxima de un subarreglo contiguo que podría contener solamente unos después de esos cambios.

# Ejemplo 1
# nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# k = 2
# # Resultado: 6

# Ejemplo 2
# nums = [0, 0, 1, 1, 1, 0, 0]
# k = 0
# # Resultado: 3

# Ejemplo 3
# nums = [0, 0, 0]
# k = 2
# # Resultado: 2

def max_subarray_with_one(nums, k):
    if len(nums) == 0:
        return 0
    
    if len(nums) <= k:
        return len(nums)
                             # [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    max_long_subarray = 0    # 0 1 2 3 4 5
    start = 0                # 0 1 2 3 4
    rest_k_numbers = k       # 2 1 0 -1 0

    for end in range(len(nums)): # 0 1 2 3 4 5 6
        if nums[end] == 0:
            rest_k_numbers -= 1

        while(rest_k_numbers < 0): 
            if nums[start] == 0:
                rest_k_numbers += 1
            
            start += 1
        
        max_long_subarray = max(max_long_subarray, end - start + 1)
        
    return max_long_subarray


print(max_subarray_with_one([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(max_subarray_with_one([0, 0, 1, 1, 1, 0, 0], 0))
print(max_subarray_with_one([0, 0, 0], 2))


# Su complejidad espacial es o(1) estamo gaurdando el valor de variables aisladas. Su complejidad temproal es 0(n) porque estamos recorriedno solo una vez el array
# La venta representa los numeros que pueden entrar en el subarray, la ventana se mueve cuando me quedo sin numeros para sustituir los 0 y me tope con otro para asi seguir revisando las otras combincaicones. 