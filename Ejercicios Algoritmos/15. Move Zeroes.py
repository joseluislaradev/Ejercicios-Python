# Move Zeroes

# Recibes una lista de números. Debes mover todos los ceros al final, manteniendo el orden de los demás elementos.

# nums = [0, 1, 0, 3, 12]

# Debe quedar:

# [1, 3, 12, 0, 0]

# Debes modificar la misma lista.

def move_zeroes(nums):
    
    next_write_index = float("inf")
    
    for i in range(0, len(nums)):
        current_num = nums[i]
        
        if current_num != 0 and next_write_index != float("inf"):
            nums[next_write_index] = current_num
            nums[i] = 0
            next_write_index += 1
        elif current_num == 0:
            next_write_index = min(next_write_index, i)

            
            

nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)
# [1, 3, 12, 0, 0]


nums = [0]
move_zeroes(nums)
print(nums)
# [0]


nums = [1, 2, 3]
move_zeroes(nums)
print(nums)
# [1, 2, 3]


nums = [0, 0, 1]
move_zeroes(nums)
print(nums)
# [1, 0, 0]