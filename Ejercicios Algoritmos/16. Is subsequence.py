# Is Subsequence

# Subsequence → /ˈsʌbˌsiː.kwəns/ → subsecuencia.

# Recibes dos strings:

# s = "abc"
# text = "ahbgdc"

# Debes devolver True cuando todos los caracteres de s aparezcan dentro de text, en el mismo orden, aunque no estén juntos.

# text = a h b g d c
#        ↑   ↑     ↑
# s    = a   b     c

# Resultado:

# True

# Pero:

# s = "axc"
# text = "ahbgdc"

# devuelve:

# False


def is_subsequence(s, text):
    
    current_index_subarray = 0
    subarray_lenght = len(s)
    
    if subarray_lenght == 0:
        return True
    
    for i in range(0, len(text)):
        if text[i] == s[current_index_subarray]:
            subarray_lenght -= 1
            current_index_subarray += 1

        if subarray_lenght == 0:
            return True 
        
    return False


print(is_subsequence("abc", "ahbgdc"))
# True

print(is_subsequence("axc", "ahbgdc"))
# False

print(is_subsequence("", "ahbgdc"))
# True

print(is_subsequence("abc", "abc"))
# True

print(is_subsequence("abc", "acb"))
# False

print(is_subsequence("aaaa", "baaab"))
# False