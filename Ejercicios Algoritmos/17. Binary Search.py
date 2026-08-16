# Problem

# You are given a sorted array of integers and a target.

# Return the index of target if it exists. Otherwise, return -1.

# nums = [-1, 0, 3, 5, 9, 12]
# target = 9

# Expected result:

# 4

# Because:

# index:  0   1  2  3  4   5
# nums:  [-1, 0, 3, 5, 9, 12]
#                     ↑
#                   target

# Another example:

# nums = [-1, 0, 3, 5, 9, 12]
# target = 2

# Result:

# -1


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        middle = (left + right) // 2

        if target < nums[middle]:
            right = middle - 1
        elif target > nums[middle]:
            left = middle + 1
        else:
            return middle
          
    return -1

print(binary_search([-1, 0, 3, 5, 9, 12], 9))
# 4

print(binary_search([-1, 0, 3, 5, 9, 12], 2))
# -1

print(binary_search([5], 5))
# 0

print(binary_search([5], 3))
# -1

print(binary_search([], 3))
# -1