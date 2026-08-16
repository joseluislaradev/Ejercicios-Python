# Problema: Two Sum II

# Recibes un arreglo ordenado ascendentemente y un objetivo target.

# Debes devolver los índices de dos números cuya suma sea exactamente target.

# Puedes asumir que existe exactamente una respuesta y no puedes usar el mismo elemento dos veces.

# Ejemplo
# nums = [2, 7, 11, 15]
# target = 9

# Resultado:

# [0, 1]

# Porque:

# nums[0] + nums[1]
# 2 + 7 = 9


def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    
    if not nums: 
        return "The array is empty"
        
    while left != right:
    
        if nums[left] + nums[right] > target:
            right -= 1
            continue
            
        if nums[left] + nums[right] < target:
            left += 1
            continue
        
        if nums[left] + nums[right] == target:
            return [left, right]
    
    return "The array not contain a correct sum"
            


print(two_sum_sorted([2, 7, 11, 15], 9))
# [0, 1]

print(two_sum_sorted([1, 2, 4, 6, 10], 8))
# [1, 3]

print(two_sum_sorted([-5, -2, 1, 3, 7], 5))
# [1, 4]

print(two_sum_sorted([3, 3], 6))
# [0, 1]

print(two_sum_sorted([], 6))
# not valid

print(two_sum_sorted([4,3], 6))
# vacio