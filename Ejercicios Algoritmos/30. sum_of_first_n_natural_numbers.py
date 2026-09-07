def sum_to_n(n):
    if n == 0:
        return n
    
    number = sum_to_n(n-1)
    return n + number

print("Case 1: sum_to_n(3)")
print("Expected: 6")
print("Actual:", sum_to_n(3))

print("\nCase 2: sum_to_n(1)")
print("Expected: 1")
print("Actual:", sum_to_n(1))

print("\nCase 3: sum_to_n(0)")
print("Expected: 0")
print("Actual:", sum_to_n(0))

print("\nCase 4: sum_to_n(5)")
print("Expected: 15")
print("Actual:", sum_to_n(5))