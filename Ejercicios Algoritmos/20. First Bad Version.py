# Problem: First Bad Version

# You have versions numbered:

# 1, 2, 3, 4, ..., n

# At some point, a version becomes bad. From that moment on, every later version is also bad.

# Example:

# version:  1  2  3  4  5  6  7
# status:   ✅ ✅ ✅ ❌ ❌ ❌ ❌
#                   ↑
#               first bad

# You have this function available:

# def is_bad(version):
#     ...

# It returns:

# True   # bad version
# False  # good version

# Your job is to implement:

# def first_bad_version(n):
#     pass

# It should return the first bad version.

# For example, imagine internally:

# is_bad(1) -> False
# is_bad(2) -> False
# is_bad(3) -> False
# is_bad(4) -> True
# is_bad(5) -> True

# Then:

# first_bad_version(5)
# # 4
# Important constraint

# Assume n can be extremely large, so we want to make as few calls to is_bad() as possible.

first_bad = 3

def is_bad(version):
    return version >= first_bad


def first_bad_version(n):
    left = 1
    right = n
    first_bad_number = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if(is_bad(mid)):
            first_bad_number = mid
            right = mid - 1 
        else: 
            left = mid + 1
        
    return first_bad_number 
    
    
print(first_bad_version(5))
