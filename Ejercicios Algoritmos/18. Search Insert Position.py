# You are given a sorted array with no duplicates and a target.

# If target exists, return its index.
# If it does not exist, return the index where it should be inserted so the array stays sorted.

# Example:

# nums = [1, 3, 5, 6]
# target = 5

# Output:

# 2

# Because 5 is already at index 2.

# Another one:

# nums = [1, 3, 5, 6]
# target = 2

# Output:

# 1

# Because inserting 2 here keeps the array sorted:

# [1, 2, 3, 5, 6]
#     ↑
#   index 1

def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    
    return left



print(search_insert([1, 3, 5, 6], 5))
# 2

print(search_insert([1, 3, 5, 6], 2))
# 1

print(search_insert([1, 3, 5, 6], 7))
# 4

print(search_insert([1, 3, 5, 6], 0))
# 0