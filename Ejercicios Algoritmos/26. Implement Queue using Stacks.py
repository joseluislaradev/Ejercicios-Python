# Next problem: Implement Queue using Stacks

# Ya conoces:

# Stack → LIFO
# Queue → FIFO

# Ahora debes construir una queue usando solo stacks.

# No puedes usar deque.

# Tu estructura debe soportar
# push(x)   # add x to the back of the queue
# pop()     # remove and return the element at the front
# peek()    # return the element at the front without removing it
# empty()   # return True if the queue is empty

# Por ejemplo:

# push(10)
# push(20)
# push(30)

# Una queue conceptualmente queda:

# front           back
#  ↓               ↓
# 10, 20, 30

# Entonces:

# peek()   # 10
# pop()    # 10
# peek()   # 20

# El problema es que un stack normalmente te daría primero:

# 30

# porque es LIFO.

# Tú tienes que descubrir cómo combinar stacks para conseguir FIFO.

# Restrictions

# Puedes utilizar:

# list.append()
# list.pop()
# list[-1]
# len()

# Pero debes tratar cada lista como un stack.

# No vale hacer:

# pop(0)

# porque estarías simulando directamente una queue y además cuesta O(n).

# Puedes usar más de un stack.

# Puedes asumir que pop() y peek() nunca se llaman cuando la queue está vacía.



class MyQueue:

    def __init__(self):
        self.stackLtoR = []
        self.stackRtoL = []

    def push(self, x):
        self.stackLtoR.append(x)
        
    def pop(self):
        if not self.stackRtoL:
            for _ in range(len(self.stackLtoR)-1, -1, -1):
                valor = self.stackLtoR.pop()
                self.stackRtoL.append(valor)
        
        return self.stackRtoL.pop()
        

    def peek(self):
        if not self.stackRtoL:
            for _ in range(len(self.stackLtoR)-1, -1, -1):
                valor = self.stackLtoR.pop()
                self.stackRtoL.append(valor)
        
        return self.stackRtoL[-1]

    def empty(self):
        return not bool(self.stackRtoL) and not bool(self.stackLtoR)
    
    
queue = MyQueue()

print(queue.empty())  # True

queue.push(10)

print(queue.empty())  # False

print(queue.pop())    # 10

print(queue.empty())  # True
 
# queue = MyQueue()

# queue.push(10)
# queue.push(20)
# queue.push(30)

# print(queue.pop())   # 10

# queue.push(40)
# queue.push(50)

# print(queue.pop())   # 20
# print(queue.pop())   # 30
# print(queue.pop())   # 40
# print(queue.pop())   # 50

#---------------------------------    
    
# queue = MyQueue()

# queue.push(10)
# queue.push(20)
# queue.push(30)

# print(queue.peek())
# # 10

# print(queue.pop())
# # 10

# print(queue.peek())
# # 20

# print(queue.empty())
# # False

# print(queue.pop())
# # 20

# print(queue.pop())
# # 30

# print(queue.empty())
# # True

#----------------

# queue = MyQueue()

# queue.push(5)
# print(queue.pop())
# # 5

# queue.push(8)
# queue.push(9)

# print(queue.peek())
# # 8