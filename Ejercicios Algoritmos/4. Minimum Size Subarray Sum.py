# Recibes:

# nums = [2, 3, 1, 2, 4, 3]
# target = 7

# Debes encontrar la longitud mínima de un subarreglo:

# contiguo;
# cuya suma sea mayor o igual que target.

# En el ejemplo:

# [4, 3]

# suma 7 y tiene longitud 2, así que el resultado es:

# 2

# Si no existe ningún subarreglo válido, debes devolver:

# 0
# Ejemplos
# target = 7
# nums = [2, 3, 1, 2, 4, 3]
# # 2
# target = 4
# nums = [1, 4, 4]
# # 1
# target = 11
# nums = [1, 1, 1, 1, 1]
# # 0



# def minimumSubarraySum(numsArray, target):
#     minimum_length = float("inf")
#     start = 0 
#     current_sum = 0

#     for end in range(len(numsArray)):
#         current_sum += end;

#         while current_sum >= target:
#             minimum_length = min(minimum_length, end - start + 1)
#             start += 1

#     if minimum_length != float("inf"):
#         return minimum_length
#     else:
#         return 0
    

# minimumSubarraySum([2, 3, 1, 2, 4, 3], 7)




def minimumSubarraySum(nums, target):

    minimum_length = float("inf")
    start = 0
    current_sum = 0

    for end in range(len(nums)):
        current_sum += nums[end]

        while current_sum >= target:
            minimum_length = min(minimum_length, end - start + 1)
            current_sum -= nums[start]
            start += 1

    return 0 if minimum_length == float("inf") else minimum_length



# print(minimumSubarraySum([2, 3, 1, 2, 4, 3], 7))
print(minimumSubarraySum([1, 4, 4], 4))
