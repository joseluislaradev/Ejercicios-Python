# <!-- Recibes una cadena s. Debes devolver la longitud del substring contiguo más largo que no tenga caracteres repetidos.

# Ejemplos
# s = "abcabcbb"
# # Resultado: 3
# # "abc"
# s = "bbbbb"
# # Resultado: 1
# # "b"
# s = "pwwkew"
# # Resultado: 3
# # "wke"

# Ten cuidado: "pwke" no cuenta porque no es contiguo.

# s = ""
# # Resultado: 0 -->


def longestSubstringWitoutRepeat(largeText):

    longest_subarray = 0
    start = 0

    for end in range(len(largeText)):

        while largeText[end] in largeText[start:end]:
            start += 1

        longest_subarray = max(longest_subarray, end - start + 1)


    return longest_subarray


print(longestSubstringWitoutRepeat("abcabcbb"))
print(longestSubstringWitoutRepeat("bbbbb"))
print(longestSubstringWitoutRepeat("pwwkew"))
print(longestSubstringWitoutRepeat(""))