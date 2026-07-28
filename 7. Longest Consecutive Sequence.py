# Problema: Longest Consecutive Sequence

# consecutive → /kənˈsek.jə.tɪv/
# Traducción: consecutivo.

# Recibes un arreglo de enteros desordenados. Debes devolver la longitud de la secuencia consecutiva más larga.

# Los números consecutivos no necesitan aparecer juntos ni en orden dentro del arreglo.

# nums = [100, 4, 200, 1, 3, 2]

# # La secuencia más larga es:
# # 1, 2, 3, 4

# # Resultado: 4

# Otros ejemplos:

# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# # Resultado: 9
# # Secuencia: 0, 1, 2, 3, 4, 5, 6, 7, 8
# nums = [1, 2, 0, 1]
# # Resultado: 3
# # Secuencia: 0, 1, 2
# nums = []
# # Resultado: 0
# Restricción importante

# Debes lograr:

# Tiempo: O(n) promedio

# Por eso no puedes ordenar el arreglo, porque:

# sorted(nums)

# costaría:

# O(n log n)




def longest_consecutive_sequence(nums):
    seen = set(nums)
    longest_sequence = 0

    for num in seen:
        # ¿num es el inicio de una secuencia?
        if num-1 not in seen:
            current_num = num
            current_length = 1

            # Avanza únicamente hacia arriba
            while current_num+1 in seen:
                current_num += 1
                current_length += 1

            longest_sequence = max(
                longest_sequence,
                current_length
            )

    return longest_sequence
    
print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))         # 4
print(longest_consecutive_sequence([1, 2, 0, 1]))                   # 3
print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # 9
print(longest_consecutive_sequence([]))                           # 0



















# def longest_consecutive_sequence(nums):
    
#     seen = set() # 1 2
#     longest_sequence = 0 # 2
#     sequence = 0 # 1 2
#     temporal_num = 0 # 1 0 1 2
    
#     for num in nums:
        
#         temporal_num = num
        
#         while temporal_num+1 in seen or temporal_num-1 in seen:
#             sequence += 1
            
#             if temporal_num+1 in seen: 
#                 temporal_num += 1 
#             else:  
#                 temporal_num -= 1
            
#         seen.add(num)
#         longest_sequence = max(longest_sequence, sequence + 1)
#         sequence = 0
            
#     return longest_sequence
    
    
# print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))         # 4
# print(longest_consecutive_sequence([1, 2, 0, 1]))                   # 3
# print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # 9
# print(longest_consecutive_sequence([[]]))                           # 0