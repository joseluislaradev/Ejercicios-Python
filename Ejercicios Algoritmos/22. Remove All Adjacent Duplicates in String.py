# You are given a string s containing lowercase English letters.

# Whenever two equal characters are next to each other, you remove both.

# You keep doing that until there are no more adjacent duplicates.

# For example:

# s = "abbaca"


# abbaca
#  ↑↑
# remove "bb"


# aaca
# ↑↑
# remove "aa"


# ca

# Output:

# "ca"

# Another example:

# "azxxzy"


# azxxzy
#   ↑↑
# → azzy
#   ↑↑
# → ay

# Output:

# "ay"
# Input / Output

# Input:

# s: str

# Return:

# str


def remove_duplicates(s):
    
    seen = []
    
    for l in s:
        if seen and l == seen[-1]:
            seen.pop()
        else: 
            seen.append(l)
            
    return "".join(seen)


print(remove_duplicates("abbaca"))
# "ca"

print(remove_duplicates("azxxzy"))
# "ay"

print(remove_duplicates("abc"))
# "abc"

print(remove_duplicates("aabb"))
# ""

print(remove_duplicates("aaaa"))
# ""

