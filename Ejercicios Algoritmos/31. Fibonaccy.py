# The Fibonacci sequence is defined as:

# F(0) = 0
# F(1) = 1
# F(n) = F(n - 1) + F(n - 2)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


print("Case 1: fibonacci(0)")
print("Expected: 0")
print("Actual:", fibonacci(0))

print("\nCase 2: fibonacci(1)")
print("Expected: 1")
print("Actual:", fibonacci(1))

print("\nCase 3: fibonacci(2)")
print("Expected: 1")
print("Actual:", fibonacci(2))

print("\nCase 4: fibonacci(6)")
print("Expected: 8")
print("Actual:", fibonacci(6))