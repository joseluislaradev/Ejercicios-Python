# Problema principal: Longest Consecutive Sequence

# Dado un arreglo de enteros desordenados, devuelve la longitud de la secuencia de números consecutivos más larga.

# Los números consecutivos no necesitan aparecer juntos ni ordenados en el arreglo.

# nums = [100, 4, 200, 1, 3, 2]

# La secuencia más larga es:

# 1, 2, 3, 4

# Resultado:

# 4
# Firma
# def longest_consecutive_sequence(nums):
#     pass
# Restricciones
# Tiempo promedio: O(n)
# Espacio: O(n)

# No puedes ordenar el arreglo, porque ordenar costaría O(n log n).


def longest_consecutive_sequence(nums):
    
    seen = set(nums)
    longest_sequence = 0
    sequence = 0
    
    for num in seen:
        
        if num - 1 not in seen:
            temporal_num = num
            sequence += 1
             
            while temporal_num + 1 in seen:
                sequence += 1
                temporal_num += 1

        longest_sequence = max(longest_sequence, sequence)
        sequence = 0
    
    return longest_sequence
    
    
print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
# 4

print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
# 9

print(longest_consecutive_sequence([10, 5, 6, 20, 7, 21]))
# 3

print(longest_consecutive_sequence([1, 2, 0, 1]))
# 3

print(longest_consecutive_sequence([]))
# 0

print(longest_consecutive_sequence([5]))
# 1



# Utilice un set inicializado con el array asi me quito los duplciados de una, para saber si un numero inicia un secuencia me fijo si existe el numero anteorior a el en el set con una consulta o(1)
# La complejidad temproal es o(n) porque tengoq ue atarvezar todo el array al menos una vez, q  ue de hecho estaba plenado recuerrer seen en lugafr de nums, creoq eu es msima compleidad en el peror caso pero con chance de recorrer menos si hubiera repetidos
# Lo de dentro es un if o(1) y se hacen varios recorrido en el while pero no se ahcen todo con cada iteracion del for, solo se ahcen en inicios de secuncai por lo qeu se suma o(n) y queda o(n)
# La complejidad espacial es o(n) porque guardo el set, las demas son vairables ailsadas o(1) que lo dejan o(n)