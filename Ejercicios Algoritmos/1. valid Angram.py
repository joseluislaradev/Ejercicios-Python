

# The dict represent the count of the letter has been seen. The time is o(n) a traverse two times but o(2n) is 0(n). Space complexity is o(n) beacuse I can keep each letter in the dict in the worst case.
# I think that is fine now. iI think tat I learn to is use the funcion get to sum element in a dict when exist o doesn't exist


def isValidAnagram(cadena1, cadena2):
    
    counts = dict()
    
    if len(cadena1) != len(cadena2):
        return False
    
    for l1 in cadena1:
        counts[l1] = counts.get(l1, 0) + 1
        
    for l2 in cadena2:
        if l2 not in counts:
            return False
        
        counts[l2] -= 1
        
        if counts[l2] == 0:
            del counts[l2] 
    
    return not counts


print(isValidAnagram("rat", "car"))