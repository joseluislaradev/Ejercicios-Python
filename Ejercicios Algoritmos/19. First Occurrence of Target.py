# Problem: First Occurrence of Target

# You are given a sorted array that may contain duplicates and a target.

# Return the index of the first occurrence of target.

# If the target does not exist, return -1.

# nums = [1, 2, 2, 2, 4, 5]
# target = 2

# Expected:

# 1

# Not 2 or 3, even though those positions also contain 2.

def first_occurrence(nums, target):
    left = 0
    right = len(nums) - 1
    index = -1

    while left <= right:
        mid = (left + right) // 2
        
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            index = mid
            right = mid - 1
            
    
    return index

print(first_occurrence([1, 2, 2, 2, 4, 5], 2))
# 1

print(first_occurrence([1, 1, 1, 1], 1))
# 0

print(first_occurrence([1, 3, 5, 7], 5))
# 2

print(first_occurrence([1, 3, 5, 7], 2))
# -1

print(first_occurrence([], 3))
# -1