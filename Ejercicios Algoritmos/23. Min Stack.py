# # Problem: Min Stack

# minimum → /ˈmɪn.ə.məm/ → mínimo

# You must design a stack that supports these operations:

# push(value)     # add a value
# pop()           # remove the most recent value
# top()           # return the most recent value
# get_min()       # return the smallest value currently in the stack

# The important requirement is that all four operations must be O(1).

# What does that mean?

# Suppose:

# push(5)
# push(2)
# push(8)

# The stack is:

# top
#  ↓
# [8]
# [2]
# [5]

# So:

# top()      # 8
# get_min()  # 2

# Then:

# pop()

# removes 8.

# Now:

# top()      # 2
# get_min()  # 2

# Then:

# pop()

# removes 2.

# Now:

# top()      # 5
# get_min()  # 5
# Important restriction

# You cannot implement get_min() by doing this every time:

# min(stack)

# because that would be:

# O(n)

# We need:

# push     O(1)
# pop      O(1)
# top      O(1)
# get_min  O(1)

# You may use additional memory.}




class MinStack:
    
    def __init__(self):
        self.min_value = []
        self.stack = []

    def push(self, value):
        if not self.min_value:
            self.min_value.append(value)
        elif self.min_value[-1] >= value:
            self.min_value.append(value)
            
        self.stack.append(value)

    def pop(self):
        value = self.stack.pop()
        if self.min_value[-1] == value: 
            self.min_value.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_value[-1]
    


stack = MinStack()

stack.push(5)
stack.push(2)
stack.push(8)

print(stack.top())      # 8
print(stack.get_min())  # 2

stack.pop()

print(stack.top())      # 2
print(stack.get_min())  # 2

stack.pop()

print(stack.top())      # 5
print(stack.get_min())  # 5



# stack = MinStack()

# stack.push(3)
# stack.push(1)
# stack.push(1)

# print(stack.get_min())  # 1

# stack.pop()

# print(stack.get_min())  # 1