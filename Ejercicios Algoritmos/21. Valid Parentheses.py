# alid Parentheses

# parentheses → /pəˈrɛn.θə.siːz/ → paréntesis.

# You receive a string containing only these characters:

# ( ) [ ] { }

# You must return True if every opening bracket is closed correctly.

# Correct:

# "()"          # True
# "()[]{}"      # True
# "{[()]}"      # True

# Incorrect:

# "(]"          # False
# "([)]"        # False
# "((("         # False
# "]"           # False

# For a string to be valid:

# 1. Every opening bracket must eventually close.
# 2. It must close with the correct type.
# 3. The order must be correct.

# For example:

# { [ ( ) ] }
#     ↑   ↑

# The ( is the last opening bracket, so it must be the first one closed.

# That's the important clue.



def is_valid(s):
    
    characters_order = []
    characters_pairs = {
        "}":"{",
        "]":"[", 
        ")":"("     
    }
    
    for c in s:
        if c not in characters_pairs:
            characters_order.append(c)
        else:
            if characters_order and characters_order[-1] == characters_pairs[c]:
                characters_order.pop() 
            else:
                return False
            
    if characters_order:
        return False
          
    return True


print(is_valid("{[()]}")) #True
print(is_valid("([)]")) # False
print(is_valid("]"))     # False
print(is_valid("((("))   # False
print(is_valid(""))      # True