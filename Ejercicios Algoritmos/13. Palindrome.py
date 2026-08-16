# Un palíndromo es una palabra que se lee igual de izquierda a derecha y de derecha a izquierda.

# radar
# reconocer
# oso

# Debes devolver True si la palabra es palíndroma y False si no.


def is_palindrome(word):
    
    left = 0
    right = len(word) - 1
    
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
        
    return True
    



print(is_palindrome("radar"))
# True

print(is_palindrome("python"))
# False

print(is_palindrome("oso"))
# True

print(is_palindrome("a"))
# True

print(is_palindrome(""))
# True