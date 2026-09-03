# Problem: Evaluate Reverse Polish Notation

# evaluate → /ɪˈvæl.ju.eɪt/ → evaluar
# operator → /ˈɑː.pə.reɪ.tɚ/ → operador

# You receive an array of strings representing a mathematical expression in Reverse Polish Notation (RPN).

# The important difference is that the operator comes after the two numbers.

# Normal expression:

# 2 + 3

# RPN:

# 2 3 +

# So:

# ["2", "3", "+"]
# → 5

# A more interesting example:

# ["2", "1", "+", "3", "*"]

# Process:

# 2 1 +
# → 3


# 3 3 *
# → 9

# Output:

# 9
# Rules

# The possible operators are:

# +
# -
# *
# /

# Whenever you encounter an operator, it applies to the two most recent unresolved numbers.

# For example:

# ["4", "13", "5", "/", "+"]

# means:

# 13 / 5 = 2
# 4 + 2 = 6

# So output:

# 6

# For division, truncate toward zero:

# 6 / -4
# → -1

# In Python, for this problem you can use:

# int(a / b)


# You can assume:

# The expression is always valid.
# There will always be exactly one final result.
# Numbers may be negative.
# You do not need to validate malformed expressions.


def eval_rpn(tokens):
    operators = {
        "+": lambda a, b: int(a + b), 
        "-": lambda a, b: int(a - b), 
        "*": lambda a, b: int(a * b), 
        "/": lambda a, b: int(a / b)
    }
    numbers = []
    
    for n in tokens:
        if n in operators:
            number2 = numbers.pop()
            number1 = numbers.pop()
            result = operators[n](number1, number2)
            numbers.append(result)
        else:
            numbers.append(int(n))
    
    return numbers[-1]


print(eval_rpn(["2", "1", "+", "3", "*"]))
# 9

print(eval_rpn(["4", "13", "5", "/", "+"]))
# 6

print(eval_rpn(["2", "3", "+"]))
# 5

print(eval_rpn(["3", "4", "-", "2", "*"]))
# -2

print(eval_rpn(["6", "-4", "/"]))
# -1

print(eval_rpn(["7"]))
# 7