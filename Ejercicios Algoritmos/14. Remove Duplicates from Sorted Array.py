# Problema: Remove Duplicates from Sorted Array

# Duplicate → /ˈduː.plɪ.kət/ → duplicado.
# In place → /ˌɪn ˈpleɪs/ → modificar la estructura original sin crear otro arreglo completo.

# Recibes un arreglo ordenado:

# nums = [1, 1, 2, 2, 3]

# Debes mover los valores únicos al comienzo del mismo arreglo:

# nums = [1, 2, 3, ?, ?]

# Los valores después de los únicos no importan. Además, debes devolver cuántos valores únicos hay:

# return 3



def remove_duplicates(nums):
        
    next_write_index = 1
    last_num = 0
    counter = 0
    if len(nums) > 0:
        last_num = nums[0] 
        counter = 1
    
    for i in range(1, len(nums)):
        if nums[i] > last_num:
            counter += 1
            last_num = nums[i]
            nums[next_write_index] = nums[i]
            next_write_index = next_write_index + 1
            
    return counter


nums = [1, 1, 2]
k = remove_duplicates(nums)
print(k)          # 2
print(nums[:k])   # [1, 2]


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(nums)
print(k)          # 5
print(nums[:k])   # [0, 1, 2, 3, 4]


nums = []
k = remove_duplicates(nums)
print(k)          # 0
print(nums[:k])   # []


nums = [7]
k = remove_duplicates(nums)
print(k)          # 1
print(nums[:k])   # [7]



# I put validation if the array it's empty or not for return 0 in that case, only becasuse I wanted test initialing my loop in number 1 index, so ignore that.
# I am traversing the array and verify if the actual num > last_num writed, because how the array is ordered is obviously that the next number to write it"s bigger, when i write i move my next_write _index one position to insert the next.
#It's o(n) in temporal complexity for the loop  and o(1) for the spacial complexity beacuse i am keeping only some variables 