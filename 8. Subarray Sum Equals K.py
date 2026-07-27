# Problema de hoy: Subarray Sum Equals K

# prefix sum → /ˈpriː.fɪks sʌm/
# cumulative sum → /ˈkjuː.mjə.lə.tɪv sʌm/

# Recibes un arreglo de enteros nums y un número k. Debes devolver cuántos subarreglos contiguos suman exactamente k.

# nums = [1, 1, 1]
# k = 2

# # [1, 1] en las posiciones 0–1
# # [1, 1] en las posiciones 1–2
# # Resultado: 2

# Otros casos:

# nums = [1, 2, 3]
# k = 3
# # [1, 2] y [3]
# # Resultado: 2
# nums = [1, -1, 0]
# k = 0
# # [1, -1], [0], [1, -1, 0]
# # Resultado: 3
# nums = []
# k = 0
# # Resultado: 0
# Restricción

# Debes buscar una solución promedio de:

# Tiempo: O(n)

# No puedes generar todos los subarreglos, porque eso sería al menos O(n²).



# def subarray_sum(nums, k):

#     subarrays_qty = 0
#     sum = 0
#     start = 0
    
#     for end in range(len(nums)): 
#         sum += nums[end]
        
#         while sum >= k: 
#             if sum == k:
#                 subarrays_qty += 1
                
#             sum -= nums[start]
#             start += 1
        
#     return subarrays_qty


# print(subarray_sum([1, 1, 1], 2)) # 2
# print(subarray_sum([1, 2, 3], 3)) # 2
# print(subarray_sum([1, -1, 0], 0)) # 3
# print(subarray_sum([], 0)) # 0




def subarray_sum(nums, k):

    subarrays_qty = 0
    sum = 0
    previous_sum = {0: 1}
    
    for num in nums: 
        sum += num
        
        subarrays_qty += previous_sum.get(sum-k, 0)
        
        previous_sum[sum] = previous_sum.get(sum, 0) + 1
        
    return subarrays_qty


print(subarray_sum([1, 1, 1], 2)) # 2
print(subarray_sum([1, 2, 3], 3)) # 2
print(subarray_sum([1, -1, 0], 0)) # 3
print(subarray_sum([1, 0, 1, 0, 1], 1)) # 8
print(subarray_sum([], 0)) # 0



