# Ransom Note

# Tienes dos cadenas:

# ransomNote: el texto que quieres construir.
# magazine: las letras disponibles.

# Cada letra de magazine puede utilizarse una sola vez.

# Devuelve True si puedes construir ransomNote; de lo contrario, devuelve False.

# ransomNote = "aa"
# magazine = "aab"
# # True
# ransomNote = "aa"
# magazine = "ab"
# # False
# ransomNote = "abc"
# magazine = "cbad"
# # True

def isPossibleBuild(ramsonNote, magazine):
        
    if len(magazine) < len(ramsonNote): 
        return False
    
    counts = dict()
    
    for l1 in magazine:
        counts[l1] = counts.get(l1, 0) + 1
        
    for l2 in ramsonNote:
        if l2 not in counts:
            return False
    
        counts[l2] -= 1
        
        if counts[l2] == 0:
            del counts[l2]
    
    return True


print(isPossibleBuild("abc","cbad"))


    
# I traverse first the ramson note because i need know the string tha i need build, keep the elements count in the dictionary, I can return false if the magazine has lower letther that the note that i will build. 
# I think that is o(n) in both complexitys. I can't return false too when the letter doesn't exist. Finally I decide how you can see traverse first maagazine because after i can know easy if one word in ramsonNote is not available in my bank of letter is false
    
    