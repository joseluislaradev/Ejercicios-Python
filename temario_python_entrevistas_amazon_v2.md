# Temario de Python para entrevistas técnicas y LeetCode — Versión 2 ampliada

**Uso recomendado:** subir este archivo a NotebookLM y pedirle quizzes, flashcards, explicaciones y entrevistas simuladas.

**Enfoque:** Python para resolver problemas tipo Amazon SDE-I, LeetCode, HackerRank y online assessments.

**Qué cambió en esta versión:**

- Se mantuvo el temario base.
- Se agregaron trucos prácticos de Python.
- Se agregaron errores comunes.
- Se agregaron plantillas rápidas de problemas.
- Se agregó una guía para pensar como entrevistado.
- Se agregó una chuleta de sintaxis.
- Se agregaron mini ejercicios y respuestas.
- Se reforzó Big O y casos borde.


**Objetivo del documento:** estudiar la sintaxis y los patrones de Python que más sirven para resolver problemas de entrevistas tipo Amazon SDE-I, LeetCode, HackerRank y online assessments.

Este archivo no intenta enseñarte "todo Python". Intenta enseñarte el Python que realmente vas a usar para resolver problemas como:

- Two Sum
- Valid Anagram
- Contains Duplicate
- Valid Parentheses
- Binary Search
- Reverse Linked List
- Number of Islands
- Rotting Oranges
- Top K Frequent Elements
- Sliding Window
- BFS / DFS
- Trees
- Heaps

---

# 1. ¿Por qué usar Python en entrevistas si yo sé TypeScript?

Python no es "más profesional" que TypeScript. TypeScript es excelente para proyectos reales: frontend, backend, APIs, React, Nest, Node, validaciones, modelos, etc.

Pero en entrevistas técnicas, especialmente con algoritmos, el objetivo suele ser este:

> Encontrar una solución correcta y eficiente en poco tiempo.

En ese contexto, Python ayuda porque tiene menos ruido sintáctico.

## Ejemplo: Two Sum en TypeScript

```ts
const seen = new Map<number, number>();

for (let i = 0; i < nums.length; i++) {
  const complement = target - nums[i];
  const previousIndex = seen.get(complement);

  if (previousIndex !== undefined) {
    return [previousIndex, i];
  }

  seen.set(nums[i], i);
}
```

## La misma lógica en Python

```python
seen = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        return [seen[complement], i]

    seen[num] = i
```

La lógica es la misma:

1. Guardar números ya vistos.
2. Calcular el complemento.
3. Revisar si el complemento ya apareció.
4. Si apareció, regresar índices.
5. Si no apareció, guardar el número actual.

Pero Python te quita ruido:

- No tienes que declarar `Map<number, number>()`.
- No tienes que pelear con `undefined`.
- No necesitas `!` o validaciones de tipos.
- Las listas, diccionarios, sets, queues y heaps son muy cómodos.
- Es rápido de escribir y explicar.

## Regla práctica

Usa:

- **Python** para entrevistas, LeetCode y online assessments.
- **TypeScript** para CV, proyectos reales, frontend/backend y trabajo profesional.

No estás "abandonando" TypeScript. Solo estás usando la herramienta más cómoda para el tipo de prueba.

---

# 2. Variables, condicionales y loops

## Variables

```python
x = 10
name = "Jose"
is_valid = True
```

En Python no pones `let`, `const`, `var` ni tipo obligatorio.

## Condicionales

```python
x = 10

if x > 5:
    print("mayor")
else:
    print("menor")
```

En Python la indentación importa. No se usan llaves `{}` como en JavaScript/TypeScript.

Mal:

```python
if x > 5:
print("mayor")
```

Bien:

```python
if x > 5:
    print("mayor")
```

## For con `range`

```python
for i in range(5):
    print(i)
```

Resultado:

```text
0
1
2
3
4
```

Ojo: `range(5)` llega hasta 4, no incluye 5.

## Recorrer una lista con índices

```python
nums = [10, 20, 30]

for i in range(len(nums)):
    print(i, nums[i])
```

Resultado:

```text
0 10
1 20
2 30
```

Esto funciona, pero en Python muchas veces se prefiere `enumerate`.

## `enumerate`

```python
nums = [10, 20, 30]

for i, num in enumerate(nums):
    print(i, num)
```

Resultado:

```text
0 10
1 20
2 30
```

`enumerate(nums)` te da dos cosas:

- `i`: índice.
- `num`: valor.

Esto es muy útil en problemas como Two Sum, porque necesitas tanto el valor como el índice.

## Cuándo usar `for num in nums`

Cuando solo necesitas el valor:

```python
for num in nums:
    print(num)
```

## Cuándo usar `for i, num in enumerate(nums)`

Cuando necesitas valor e índice:

```python
for i, num in enumerate(nums):
    print(i, num)
```

## While

```python
x = 5

while x > 0:
    print(x)
    x -= 1
```

Resultado:

```text
5
4
3
2
1
```

El `while` se usa mucho cuando controlas dos punteros, una ventana o una condición que puede cambiar dentro del loop.

---

# 3. Listas

En Python, las listas son el equivalente más común a los arrays.

```python
nums = [1, 2, 3]
```

## Operaciones básicas

```python
nums.append(4)      # agrega al final
nums.pop()          # quita y regresa el último
nums[0]             # primer elemento
nums[-1]            # último elemento
len(nums)           # tamaño
```

Ejemplo:

```python
nums = [1, 2, 3]

nums.append(4)
print(nums)  # [1, 2, 3, 4]

last = nums.pop()
print(last)  # 4
print(nums)  # [1, 2, 3]
```

## Índices negativos

```python
nums = [10, 20, 30, 40]

print(nums[-1])  # 40
print(nums[-2])  # 30
```

`-1` significa "el último".

Esto sirve mucho para stacks:

```python
stack = [1, 2, 3]
top = stack[-1]
```

---

# 4. Slicing

El slicing sirve para sacar una parte de una lista o string.

Forma general:

```python
lista[inicio:fin:paso]
```

Donde:

- `inicio`: desde dónde empiezas.
- `fin`: hasta dónde llegas, pero no lo incluye.
- `paso`: de cuánto en cuánto avanzas.

## Ejemplo base

```python
nums = [10, 20, 30, 40, 50, 60]
```

Índices:

```text
índice:  0   1   2   3   4   5
valor:  10  20  30  40  50  60
```

## `nums[1:4]`

```python
nums[1:4]
```

Significa:

> Dame los elementos desde el índice 1 hasta antes del índice 4.

Resultado:

```python
[20, 30, 40]
```

Incluye:

- índice 1
- índice 2
- índice 3

No incluye:

- índice 4

Regla importante:

> En `nums[a:b]`, `a` sí entra y `b` no entra.

## `nums[:3]`

```python
nums[:3]
```

Significa:

> Desde el inicio hasta antes del índice 3.

Resultado:

```python
[10, 20, 30]
```

## `nums[2:]`

```python
nums[2:]
```

Significa:

> Desde el índice 2 hasta el final.

Resultado:

```python
[30, 40, 50, 60]
```

## `nums[::2]`

```python
nums[::2]
```

Significa:

> Recorre desde el inicio hasta el final, saltando de 2 en 2.

Resultado:

```python
[10, 30, 50]
```

## `nums[::-1]`

```python
nums[::-1]
```

Significa:

> Recorre la lista al revés.

Resultado:

```python
[60, 50, 40, 30, 20, 10]
```

Esto también sirve con strings:

```python
s = "hello"
print(s[::-1])
```

Resultado:

```text
olleh
```

## Slicing para rotar arrays

Problema: rotar a la izquierda.

```python
a = [1, 2, 3, 4, 5]
d = 2
```

Resultado esperado:

```python
[3, 4, 5, 1, 2]
```

Solución:

```python
def rotLeft(a, d):
    d = d % len(a)
    return a[d:] + a[:d]
```

Explicación:

```python
a[d:]   # [3, 4, 5]
a[:d]   # [1, 2]
```

Juntas las dos partes:

```python
[3, 4, 5] + [1, 2]
```

Resultado:

```python
[3, 4, 5, 1, 2]
```

---

# 5. Matrices

En Python, una matriz normalmente es una lista de listas.

Ejemplo 3x3:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Piensa en una matriz como Excel:

```text
fila 0: 1  2  3
fila 1: 4  5  6
fila 2: 7  8  9
```

Para acceder a un valor:

```python
matrix[fila][columna]
```

Ejemplo:

```python
print(matrix[1][2])
```

Resultado:

```text
6
```

Porque:

- fila 1 es `[4, 5, 6]`
- columna 2 dentro de esa fila es `6`

## Índices de la matriz

```text
matrix[0][0] = 1
matrix[0][1] = 2
matrix[0][2] = 3

matrix[1][0] = 4
matrix[1][1] = 5
matrix[1][2] = 6

matrix[2][0] = 7
matrix[2][1] = 8
matrix[2][2] = 9
```

## Crear una matriz de ceros

```python
rows = 3
cols = 4

matrix = [[0] * cols for _ in range(rows)]
```

Resultado:

```python
[
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
```

## ¿Qué significa `_`?

```python
for _ in range(rows)
```

El `_` significa:

> No me importa el valor de la variable, solo quiero repetir algo.

Es decir:

```python
[[0] * cols for _ in range(rows)]
```

Significa:

> Crea una fila de ceros, repítela `rows` veces.

## Error común al crear matrices

No hagas esto:

```python
matrix = [[0] * cols] * rows
```

Parece que funciona, pero tiene una trampa.

Ejemplo:

```python
rows = 3
cols = 4

matrix = [[0] * cols] * rows
matrix[0][0] = 1

print(matrix)
```

Uno esperaría:

```python
[
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
```

Pero sale:

```python
[
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]
```

¿Por qué?

Porque las filas no son independientes. Las tres filas apuntan a la misma lista en memoria.

Regla:

```python
matrix = [[0] * cols for _ in range(rows)]  # bien
matrix = [[0] * cols] * rows                # evita esto
```

## Recorrer una matriz

```python
rows = len(matrix)
cols = len(matrix[0])

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c])
```

Donde:

- `r` = row = fila
- `c` = column = columna

Esto aparece mucho en problemas como:

- Number of Islands
- Flood Fill
- Rotting Oranges
- Word Search
- Matrix BFS / DFS

---

# 6. Diccionarios (`dict`)

Un diccionario en Python es parecido a un `Map` en TypeScript.

Sirve para guardar pares:

```text
clave -> valor
```

Ejemplo:

```python
seen = {}

seen[5] = 0
```

Aquí guardaste:

```text
5 -> 0
```

## Revisar si una clave existe

```python
if 5 in seen:
    print(seen[5])
```

Ojo: `in` en un diccionario revisa las claves, no los valores.

## Ejemplo: Two Sum

```python
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
```

Explicación:

- `seen` guarda números que ya viste.
- La clave es el número.
- El valor es su índice.

Ejemplo:

```python
nums = [2, 7, 11, 15]
target = 9
```

Paso 1:

```text
num = 2
complement = 7
7 no está en seen
guardo 2 -> índice 0
```

Paso 2:

```text
num = 7
complement = 2
2 sí está en seen
return [0, 1]
```

## Contar frecuencias

```python
count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
```

Forma más corta:

```python
count[num] = count.get(num, 0) + 1
```

## ¿Qué hace `.get()`?

```python
count.get(num, 0)
```

Significa:

> Dame `count[num]` si existe. Si no existe, dame 0.

Ejemplo:

```python
count = {}

num = 5
count[num] = count.get(num, 0) + 1
```

Como `5` no existe todavía:

```python
count.get(5, 0)
```

regresa `0`.

Entonces:

```python
count[5] = 0 + 1
```

Resultado:

```python
{5: 1}
```

## Ejemplo: Valid Anagram

Tu solución fue de este estilo:

```python
def isAnagram(s, t):
    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if char not in counts:
            return False

        counts[char] -= 1

        if counts[char] == 0:
            del counts[char]

    return not counts
```

Idea:

1. Cuentas letras de `s`.
2. Restas letras de `t`.
3. Si al final no queda nada, son anagramas.

Complejidad:

```text
Tiempo: O(n)
Espacio: O(k)
```

Donde `k` es la cantidad de caracteres distintos.

---

# 7. Sets

Un `set` es una colección donde no hay duplicados.

Sirve cuando solo te importa saber si algo ya apareció.

```python
visited = set()

visited.add(5)

if 5 in visited:
    print("ya existe")
```

## Diferencia entre `dict` y `set`

Usa `dict` si necesitas guardar una relación:

```text
número -> índice
letra -> conteo
nodo -> distancia
```

Usa `set` si solo necesitas existencia:

```text
¿ya lo vi?
¿ya lo visité?
¿ya existe?
```

## Ejemplo: Contains Duplicate

```python
def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False
```

Idea:

1. Recorres los números.
2. Si el número ya está en `seen`, hay duplicado.
3. Si no está, lo agregas.
4. Si terminas sin repetir, no hay duplicado.

Complejidad:

```text
Tiempo: O(n)
Espacio: O(n)
```

## Tu solución con diccionario

```python
seen = {}

for num in nums:
    if num in seen:
        return True

    seen[num] = 1

return False
```

También está bien. Pero `set` comunica mejor la intención porque no necesitas guardar valor.

---

# 8. `defaultdict` y `Counter`

Se importan desde `collections`.

```python
from collections import defaultdict, Counter
```

## `defaultdict`

`defaultdict` sirve cuando quieres evitar estar preguntando si una clave existe.

Ejemplo normal:

```python
graph = {}

if 1 not in graph:
    graph[1] = []

graph[1].append(2)
```

Con `defaultdict(list)`:

```python
from collections import defaultdict

graph = defaultdict(list)

graph[1].append(2)
graph[1].append(3)
```

Si `graph[1]` no existe, Python crea automáticamente una lista vacía.

Resultado:

```python
{
    1: [2, 3]
}
```

Muy usado para grafos:

```python
graph = defaultdict(list)

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
```

## `Counter`

`Counter` cuenta frecuencias automáticamente.

```python
from collections import Counter

count = Counter("banana")
print(count)
```

Resultado:

```python
Counter({'a': 3, 'n': 2, 'b': 1})
```

También sirve con listas:

```python
nums = [1, 1, 2, 3, 3, 3]

count = Counter(nums)
print(count)
```

Resultado:

```python
Counter({3: 3, 1: 2, 2: 1})
```

## Valid Anagram con Counter

```python
from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)
```

Esto es muy corto y correcto, pero para entrevista conviene entender la versión manual con diccionario.

---

# 9. Queue con `deque`

Una queue es una estructura FIFO:

```text
First In, First Out
```

El primero que entra es el primero que sale.

En Python se usa `deque`.

```python
from collections import deque

q = deque()

q.append(1)
q.append(2)

x = q.popleft()
```

Después de `popleft`, `x` vale `1`.

## ¿Por qué no usar lista?

Podrías hacer:

```python
arr = [1, 2, 3]
x = arr.pop(0)
```

Pero `pop(0)` es lento porque Python tiene que mover todos los elementos hacia la izquierda.

```text
pop(0) en lista: O(n)
popleft() en deque: O(1)
```

## BFS

`deque` se usa muchísimo en BFS.

```python
from collections import deque

q = deque([start])
visited = set([start])

while q:
    node = q.popleft()

    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            q.append(nei)
```

BFS sirve para:

- caminos más cortos en grafos sin pesos
- niveles en árboles
- matrices
- expansión por capas

## Tu problema de Array Left Rotation con deque

Tu idea:

```python
from collections import deque

def rotLeft(a, d):
    cola = deque(a)

    for i in range(d):
        element = cola.popleft()
        cola.append(element)

    return list(cola)
```

Funciona porque:

- sacas el primer elemento
- lo mandas al final
- repites `d` veces

Mejora:

```python
from collections import deque

def rotLeft(a, d):
    cola = deque(a)
    d = d % len(a)

    for _ in range(d):
        element = cola.popleft()
        cola.append(element)

    return list(cola)
```

¿Por qué `d % len(a)`?

Porque rotar una lista de tamaño 5 por 5 posiciones la deja igual.

Rotar por 7 es lo mismo que rotar por 2.

---

# 10. Stack

Un stack es LIFO:

```text
Last In, First Out
```

El último que entra es el primero que sale.

En Python una lista sirve como stack.

```python
stack = []

stack.append(1)
stack.append(2)

top = stack.pop()
```

`top` vale `2`.

## Ver el último sin sacarlo

```python
stack[-1]
```

## Ejemplo: Valid Parentheses

```python
def isValid(s):
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return not stack
```

Idea:

- Si es apertura, lo guardas.
- Si es cierre, debe coincidir con el último abierto.
- Si al final no queda nada en stack, es válido.

---

# 11. Heap / Priority Queue

En Python se usa `heapq`.

```python
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

smallest = heapq.heappop(heap)
```

`smallest` vale `2`.

Python usa min heap por defecto:

> Siempre sale el elemento más pequeño.

## Max heap

Para simular un max heap, metes negativos.

```python
import heapq

heap = []

for num in [5, 2, 8]:
    heapq.heappush(heap, -num)

max_num = -heapq.heappop(heap)
```

`max_num` vale `8`.

## Problemas donde aparece heap

- Top K Frequent Elements
- K Closest Points to Origin
- Merge K Sorted Lists
- Find Median from Data Stream

---

# 12. Strings

Un string se puede recorrer como lista de caracteres.

```python
s = "hello"

print(s[0])   # h
print(s[-1])  # o
print(len(s)) # 5
```

## Recorrer caracteres

```python
for ch in s:
    print(ch)
```

## Convertir a minúsculas o mayúsculas

```python
s.lower()
s.upper()
```

## Reversa

```python
s[::-1]
```

## Separar palabras

```python
sentence = "hello world"
words = sentence.split()
```

Resultado:

```python
["hello", "world"]
```

## Unir caracteres o palabras

```python
chars = ["h", "i"]
word = "".join(chars)
```

Resultado:

```python
"hi"
```

Con espacio:

```python
words = ["hello", "world"]
sentence = " ".join(words)
```

Resultado:

```python
"hello world"
```

## Valid Palindrome

```python
def isPalindrome(s):
    cleaned = []

    for char in s:
        if char.isalnum():
            cleaned.append(char.lower())

    cleaned = "".join(cleaned)

    return cleaned == cleaned[::-1]
```

Métodos útiles:

```python
char.isalnum()  # letra o número
char.isalpha()  # letra
char.isdigit()  # número
char.lower()    # minúscula
```

---

# 13. Sorting

## Ordenar modificando la lista

```python
nums = [3, 1, 2]
nums.sort()

print(nums)  # [1, 2, 3]
```

## Crear una lista ordenada nueva

```python
nums = [3, 1, 2]
sorted_nums = sorted(nums)

print(sorted_nums)  # [1, 2, 3]
print(nums)         # [3, 1, 2]
```

## Orden descendente

```python
nums.sort(reverse=True)
```

## Ordenar por una propiedad

```python
pairs = [[1, 5], [2, 3], [4, 1]]

pairs.sort(key=lambda x: x[1])
```

Ordena por el segundo valor de cada par.

Resultado:

```python
[[4, 1], [2, 3], [1, 5]]
```

## Intervals

Muy común:

```python
intervals.sort(key=lambda x: x[0])
```

Ordena intervalos por el inicio.

Ejemplo:

```python
intervals = [[5, 7], [1, 3], [2, 6]]
intervals.sort(key=lambda x: x[0])
```

Resultado:

```python
[[1, 3], [2, 6], [5, 7]]
```

---

# 14. Funciones y tipos opcionales

## Función simple

```python
def twoSum(nums, target):
    return []
```

## Con tipos estilo LeetCode

```python
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    return []
```

Los tipos ayudan a leer, pero en Python no son obligatorios para que corra.

## Clase estilo LeetCode

LeetCode suele darte esto:

```python
class Solution(object):
    def twoSum(self, nums, target):
        pass
```

O en Python 3:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass
```

Tú normalmente solo editas el método.

---

# 15. Recursión

Recursión es cuando una función se llama a sí misma.

Se usa mucho en árboles y DFS.

## Estructura general

```python
def dfs(node):
    if not node:
        return

    dfs(node.left)
    dfs(node.right)
```

La parte importante es el caso base:

```python
if not node:
    return
```

Sin caso base, la recursión no sabe cuándo detenerse.

## Ejemplo: Maximum Depth of Binary Tree

```python
def maxDepth(root):
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

Explicación:

- Si el nodo está vacío, profundidad 0.
- Si existe, cuenta 1 por el nodo actual.
- Luego toma el máximo entre izquierda y derecha.

---

# 16. Linked List y Trees

LeetCode normalmente ya te da estas clases, pero debes entenderlas.

## Linked List

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Una linked list no se accede por índice como una lista normal.

No haces:

```python
head[0]
```

En linked list recorres con punteros:

```python
curr = head

while curr:
    print(curr.val)
    curr = curr.next
```

## Reverse Linked List

```python
def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev
```

Idea:

- `prev`: lo que ya quedó invertido.
- `curr`: nodo actual.
- `next_node`: guardas el siguiente antes de romper el enlace.

## TreeNode

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Un árbol se recorre con DFS o BFS.

---

# 17. Infinito y comparaciones

A veces necesitas iniciar un mínimo o máximo.

```python
best = float("inf")
worst = float("-inf")
```

Ejemplo:

```python
nums = [5, 2, 8]

min_val = float("inf")

for num in nums:
    if num < min_val:
        min_val = num
```

Resultado:

```python
2
```

También existen:

```python
min(a, b)
max(a, b)
```

---

# 18. Patrones principales para entrevistas

Esta parte es más importante que memorizar sintaxis suelta.

## 18.1 Hash Map

Se usa cuando necesitas:

- contar frecuencias
- buscar complementos
- guardar índices
- agrupar cosas

Plantilla:

```python
seen = {}

for i, num in enumerate(nums):
    if algo in seen:
        return ...

    seen[num] = i
```

Problemas:

- Two Sum
- Valid Anagram
- Group Anagrams
- Top K Frequent Elements

## 18.2 Set de visitados

Se usa cuando necesitas saber si algo ya apareció o ya fue visitado.

```python
visited = set()

for num in nums:
    if num in visited:
        return True

    visited.add(num)
```

Problemas:

- Contains Duplicate
- Graph traversal
- Number of Islands
- Longest Consecutive Sequence

## 18.3 Two Pointers

Usas dos índices, normalmente uno a la izquierda y otro a la derecha.

```python
l = 0
r = len(nums) - 1

while l < r:
    if condition:
        l += 1
    else:
        r -= 1
```

Problemas:

- Valid Palindrome
- Two Sum II
- Container With Most Water
- 3Sum

## 18.4 Sliding Window

Usas una ventana que crece y se contrae.

```python
l = 0

for r in range(len(nums)):
    # agregar nums[r] a la ventana

    while condition:
        # quitar nums[l] de la ventana
        l += 1
```

Problemas:

- Longest Substring Without Repeating Characters
- Best Time to Buy and Sell Stock
- Minimum Window Substring
- Maximum Average Subarray

## 18.5 Stack

```python
stack = []

for char in s:
    if condition:
        stack.append(char)
    else:
        stack.pop()
```

Problemas:

- Valid Parentheses
- Min Stack
- Daily Temperatures
- Evaluate Reverse Polish Notation

## 18.6 BFS

```python
from collections import deque

q = deque([start])
visited = set([start])

while q:
    node = q.popleft()

    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            q.append(nei)
```

Problemas:

- Level Order Traversal
- Rotting Oranges
- Number of Islands
- Shortest Path in Grid

## 18.7 DFS

Recursivo:

```python
def dfs(node):
    if node in visited:
        return

    visited.add(node)

    for nei in graph[node]:
        dfs(nei)
```

En matrices:

```python
def dfs(r, c):
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return

    if grid[r][c] == "0":
        return

    grid[r][c] = "0"

    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)
```

Problemas:

- Number of Islands
- Clone Graph
- Max Area of Island
- Trees

## 18.8 Heap

```python
import heapq

heap = []

heapq.heappush(heap, value)
smallest = heapq.heappop(heap)
```

Problemas:

- Top K Frequent Elements
- K Closest Points
- Merge K Sorted Lists

---

# 19. Complejidad Big O básica

## O(1)

Tiempo constante.

```python
nums[0]
seen[num]
```

Acceder a un diccionario o set normalmente es O(1) promedio.

## O(n)

Recorres la entrada una vez.

```python
for num in nums:
    print(num)
```

## O(n²)

Dos loops anidados sobre la misma entrada.

```python
for i in range(len(nums)):
    for j in range(len(nums)):
        print(nums[i], nums[j])
```

## O(log n)

Cuando partes el problema a la mitad.

Ejemplo:

```python
binary search
```

## O(n log n)

Muy común en sorting.

```python
nums.sort()
```

## Espacio

Si creas un diccionario, set o lista extra que puede crecer con la entrada:

```python
seen = set()
```

Espacio:

```text
O(n)
```

Si solo usas variables:

```python
left = 0
right = len(nums) - 1
```

Espacio:

```text
O(1)
```

---

# 20. Tus problemas resueltos y qué patrón usaste

## Two Sum

Tu primera solución fue fuerza bruta con doble loop.

Complejidad:

```text
O(n²)
```

Luego aprendiste la solución con hash map.

Patrón:

```text
Hash Map
```

## Valid Anagram

Tu solución con diccionario de conteos fue buena.

Patrón:

```text
Hash Map / Frequency Count
```

Idea:

- contar letras de `s`
- restar letras de `t`
- si queda vacío, son anagramas

## Contains Duplicate

Tu solución con diccionario funcionó.

Patrón:

```text
Set / Hash Map
```

Mejor versión conceptual:

```python
seen = set()

for num in nums:
    if num in seen:
        return True
    seen.add(num)

return False
```

## Array Left Rotation

Tu solución con `deque` funcionó.

Patrón:

```text
Queue / Deque
```

También aprendiste una forma con slicing:

```python
def rotLeft(a, d):
    d = d % len(a)
    return a[d:] + a[:d]
```

---

# 21. Orden recomendado para estudiar

No estudies Python como si fuera un curso enorme.

Estúdialo en este orden:

1. Variables, `if`, `for`, `while`
2. Listas
3. Slicing
4. Diccionarios
5. Sets
6. Strings
7. `deque`
8. Stack con lista
9. `Counter` y `defaultdict`
10. Sorting con `lambda`
11. Recursión
12. Linked List
13. Trees
14. Heap

---

# 22. Mini plan de práctica

## Día 1

Conceptos:

- listas
- dict
- set
- enumerate

Problemas:

- Two Sum
- Contains Duplicate
- Valid Anagram

## Día 2

Conceptos:

- strings
- slicing
- two pointers

Problemas:

- Valid Palindrome
- Reverse String
- Two Sum II

## Día 3

Conceptos:

- stack
- deque

Problemas:

- Valid Parentheses
- Min Stack
- Array Left Rotation

## Día 4

Conceptos:

- binary search
- sorting

Problemas:

- Binary Search
- Search Insert Position
- Merge Intervals

## Día 5

Conceptos:

- recursion
- linked list

Problemas:

- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle

## Día 6

Conceptos:

- trees
- DFS
- BFS

Problemas:

- Maximum Depth of Binary Tree
- Invert Binary Tree
- Binary Tree Level Order Traversal

## Día 7

Conceptos:

- matrices
- BFS/DFS en grid

Problemas:

- Number of Islands
- Flood Fill
- Rotting Oranges

---

# 23. Frases para explicar soluciones en entrevista

## Hash map

```text
I use a hash map to store values I have already seen. This allows me to check if a complement or a repeated value exists in constant time.
```

## Set

```text
I use a set because I only need to know whether a value has appeared before.
```

## Frequency count

```text
I count the frequency of each character and then compare or decrement the counts.
```

## Two pointers

```text
I use two pointers, one at the beginning and one at the end, and move them depending on the condition.
```

## Sliding window

```text
I use a sliding window to keep track of a valid range while expanding and shrinking the window.
```

## BFS

```text
I use BFS because I want to process nodes level by level.
```

## DFS

```text
I use DFS to explore as far as possible before backtracking.
```

## Complexity

```text
The time complexity is O(n) because I visit each element once.
The space complexity is O(n) because I store values in a hash map.
```

---

# 24. Checklist rápida antes de resolver un problema

Antes de escribir código, pregúntate:

1. ¿Necesito saber si algo ya apareció?
   - Usa `set`.

2. ¿Necesito guardar valor asociado?
   - Usa `dict`.

3. ¿Necesito contar frecuencias?
   - Usa `dict` o `Counter`.

4. ¿Necesito sacar elementos en orden FIFO?
   - Usa `deque`.

5. ¿Necesito el último que entró?
   - Usa stack con lista.

6. ¿La lista está ordenada?
   - Piensa en binary search o two pointers.

7. ¿Es substring/subarray continuo?
   - Piensa en sliding window.

8. ¿Es árbol?
   - Piensa en DFS o BFS.

9. ¿Es matriz?
   - Piensa en filas, columnas, límites y visited.

10. ¿Piden top K, menor, mayor, prioridad?
   - Piensa en heap.

---

# 25. Errores típicos que debes evitar

## Usar `pop(0)` en listas para queue

Evita:

```python
arr.pop(0)
```

Mejor:

```python
from collections import deque
q = deque()
q.popleft()
```

## Crear matriz mal

Evita:

```python
matrix = [[0] * cols] * rows
```

Mejor:

```python
matrix = [[0] * cols for _ in range(rows)]
```

## Usar `enumerate` cuando no necesitas índice

Evita:

```python
for i, num in enumerate(nums):
    print(num)
```

Mejor:

```python
for num in nums:
    print(num)
```

Usa `enumerate` solo si necesitas `i`.

## Olvidar que el final del slicing no entra

```python
nums[1:4]
```

Incluye 1, 2, 3. No incluye 4.

## Confundir `dict` y `set`

Si solo necesitas saber si existe:

```python
seen = set()
```

Si necesitas guardar información:

```python
seen = {}
```

---

# 26. Resumen ultra corto

Para entrevistas, aprende bien esto:

```python
# lista
nums = [1, 2, 3]
nums.append(4)
nums.pop()

# dict
seen = {}
seen[num] = i
if num in seen:
    ...

# set
visited = set()
visited.add(num)

# enumerate
for i, num in enumerate(nums):
    ...

# slicing
nums[1:4]
nums[::-1]

# deque
from collections import deque
q = deque()
q.append(x)
q.popleft()

# stack
stack = []
stack.append(x)
stack.pop()

# counter
from collections import Counter
count = Counter(nums)

# defaultdict
from collections import defaultdict
graph = defaultdict(list)

# heap
import heapq
heapq.heappush(heap, x)
heapq.heappop(heap)
```

Si dominas eso, ya tienes la base para la mayoría de problemas tipo Amazon SDE-I.

---

# 27. Cómo usar este documento en NotebookLM

Puedes pedirle cosas como:

- "Explícame slicing con más ejemplos."
- "Hazme ejercicios de dict y set."
- "Pregúntame como entrevista técnica sobre Two Sum."
- "Dame 10 ejercicios para practicar matrices."
- "Explícame BFS usando una matriz."
- "Hazme flashcards de este documento."
- "Hazme un examen corto de Python para LeetCode."
- "Crea una tabla con patrón, estructura de datos y problemas típicos."

La idea no es memorizar todo en un día. La idea es reconocer patrones y poder escribir código sin trabarte con la sintaxis.





---

# 28. Cómo pensar como entrevistado, no solo como programador

En entrevistas técnicas no basta con llegar al código. También importa que puedas explicar tu razonamiento.

Tu proceso debería verse así:

1. Entiendo el problema.
2. Pregunto o aclaro casos borde.
3. Propongo una solución simple.
4. Analizo complejidad.
5. Optimizo si hace falta.
6. Codifico.
7. Pruebo con ejemplos.
8. Explico el resultado.

## Plantilla mental antes de escribir código

Antes de codificar, di mentalmente:

```text
Input:
Output:
Restricciones:
Casos borde:
Patrón probable:
Estructura de datos:
Complejidad esperada:
```

Ejemplo con Contains Duplicate:

```text
Input: lista de números
Output: True si algún número se repite
Restricciones: puede tener muchos elementos
Casos borde: lista vacía, un solo elemento, todos únicos
Patrón probable: set
Estructura de datos: set para valores vistos
Complejidad esperada: O(n) tiempo, O(n) espacio
```

Luego ya escribes.

---

# 29. Cómo elegir estructura de datos rápidamente

Esta tabla sirve como mapa mental.

| Pregunta | Estructura probable | Ejemplos |
|---|---|---|
| ¿Necesito saber si algo ya apareció? | `set` | Contains Duplicate |
| ¿Necesito guardar valor asociado? | `dict` | Two Sum |
| ¿Necesito contar frecuencia? | `dict` / `Counter` | Valid Anagram |
| ¿Necesito procesar por orden de llegada? | `deque` | BFS |
| ¿Necesito último que entró? | `stack` con lista | Valid Parentheses |
| ¿Necesito menor/mayor rápido? | `heapq` | Top K |
| ¿Tengo lista ordenada? | binary search / two pointers | Two Sum II |
| ¿Es subarray/substring continuo? | sliding window | Longest Substring |
| ¿Es árbol? | DFS / BFS | Max Depth |
| ¿Es matriz? | BFS / DFS + límites | Number of Islands |

---

# 30. Truquitos de Python para LeetCode

## 30.1 `if not lista`

En Python, una lista vacía se evalúa como `False`.

```python
stack = []

if not stack:
    print("está vacío")
```

También aplica para:

```python
if not counts:
    return True
```

Esto significa que el diccionario está vacío.

## 30.2 `dict.get`

En lugar de:

```python
if char in count:
    count[char] += 1
else:
    count[char] = 1
```

Puedes hacer:

```python
count[char] = count.get(char, 0) + 1
```

## 30.3 `set(nums)`

Convierte una lista a set y elimina duplicados.

```python
nums = [1, 2, 2, 3]
unique = set(nums)

print(unique)  # {1, 2, 3}
```

Contains Duplicate en una línea:

```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```

Para entrevista, la versión con loop puede ser mejor para explicar, pero esta es válida.

## 30.4 Intercambio de variables

En Python puedes intercambiar sin variable temporal:

```python
a, b = b, a
```

Útil en algunos problemas.

## 30.5 Asignación múltiple

```python
left, right = 0, len(nums) - 1
```

Más limpio que:

```python
left = 0
right = len(nums) - 1
```

## 30.6 `in` es poderoso

Con lista:

```python
x in nums
```

puede ser O(n).

Con set o dict:

```python
x in seen
```

normalmente es O(1) promedio.

Por eso `set` y `dict` son tan importantes.

## 30.7 Cuidado con strings

Los strings son inmutables.

Esto no se puede hacer:

```python
s[0] = "H"
```

Si necesitas modificar caracteres, convierte a lista:

```python
chars = list(s)
chars[0] = "H"
s = "".join(chars)
```

## 30.8 `ord` y `chr`

Útiles para problemas con letras.

```python
ord("a")  # 97
ord("b")  # 98
chr(97)   # 'a'
```

Ejemplo: índice de letra minúscula:

```python
idx = ord(char) - ord("a")
```

Si `char = "c"`:

```python
idx = 2
```

Esto sirve para arrays de 26 posiciones.

## 30.9 Array de frecuencia para letras

Si el problema solo usa letras minúsculas `a-z`, puedes usar lista de 26.

```python
count = [0] * 26

for char in s:
    idx = ord(char) - ord("a")
    count[idx] += 1
```

Esto puede ser más eficiente que dict, pero dict es más flexible y más fácil al inicio.

## 30.10 `zip`

Recorre dos listas al mismo tiempo.

```python
a = [1, 2, 3]
b = ["a", "b", "c"]

for num, letter in zip(a, b):
    print(num, letter)
```

Resultado:

```text
1 a
2 b
3 c
```

## 30.11 `reversed`

```python
nums = [1, 2, 3]

for num in reversed(nums):
    print(num)
```

No crea necesariamente una lista nueva como `nums[::-1]` para iterar.

## 30.12 `any` y `all`

```python
any([False, True, False])  # True
all([True, True, False])   # False
```

Ejemplo:

```python
if all(x > 0 for x in nums):
    print("todos positivos")
```

No son necesarios para empezar, pero ayudan a leer código.

---

# 31. Errores silenciosos comunes en Python

## 31.1 Usar variable equivocada en loops

```python
for i, num in enumerate(nums):
    print(i)
```

Si no usas `i`, no uses `enumerate`.

Mejor:

```python
for num in nums:
    print(num)
```

## 31.2 Modificar lista mientras la recorres

Evita esto:

```python
for num in nums:
    if num < 0:
        nums.remove(num)
```

Puede saltarse elementos.

Mejor crea otra lista:

```python
filtered = []

for num in nums:
    if num >= 0:
        filtered.append(num)
```

O usa comprensión:

```python
filtered = [num for num in nums if num >= 0]
```

## 31.3 Confundir `is` con `==`

Usa `==` para comparar valores.

```python
if a == b:
    ...
```

`is` compara identidad de objeto, no igualdad de valor. En LeetCode casi siempre quieres `==`.

## 31.4 Olvidar regresar algo

En Python, si no haces `return`, la función regresa `None`.

```python
def f():
    x = 10

print(f())  # None
```

## 31.5 Off-by-one

Error clásico: pasarte o quedarte corto por 1.

Recuerda:

```python
range(n)       # 0 a n-1
nums[a:b]      # a entra, b no entra
```

## 31.6 Variables compartidas en matrices

Ya lo vimos, pero es muy importante:

Mal:

```python
matrix = [[0] * cols] * rows
```

Bien:

```python
matrix = [[0] * cols for _ in range(rows)]
```

## 31.7 Usar `pop(0)` en queue

Mal para BFS:

```python
queue.pop(0)
```

Mejor:

```python
from collections import deque
queue.popleft()
```

---

# 32. Comprensiones de listas

Las comprensiones de listas te permiten crear listas de forma compacta.

## Forma básica

```python
squares = []

for x in nums:
    squares.append(x * x)
```

Equivalente:

```python
squares = [x * x for x in nums]
```

## Con condición

```python
evens = [x for x in nums if x % 2 == 0]
```

## Cuándo usarlas

Úsalas si mejoran la claridad.

Bien:

```python
cleaned = [char.lower() for char in s if char.isalnum()]
```

Demasiado complejo:

```python
result = [x+y for x in a for y in b if x+y > 10 and x-y < 3]
```

En entrevista, claridad gana.

---

# 33. Plantillas rápidas de problemas comunes

## 33.1 Binary Search

```python
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

Complejidad:

```text
Tiempo: O(log n)
Espacio: O(1)
```

Truco:

```python
mid = (left + right) // 2
```

En Python no hay overflow práctico como en otros lenguajes para enteros grandes, pero en Java/C++ a veces usan:

```python
mid = left + (right - left) // 2
```

## 33.2 Two Pointers en string

```python
def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True
```

## 33.3 Sliding Window sin repetidos

```python
def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    best = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        best = max(best, right - left + 1)

    return best
```

Idea:

- `right` expande la ventana.
- `left` la contrae si hay repetidos.
- `seen` guarda caracteres actuales dentro de la ventana.

## 33.4 DFS en matriz

```python
def dfs(r, c):
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return

    if grid[r][c] == "0":
        return

    grid[r][c] = "0"

    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)
```

Truco:

```python
directions = [(1,0), (-1,0), (0,1), (0,-1)]
```

Con directions:

```python
for dr, dc in directions:
    nr = r + dr
    nc = c + dc
```

## 33.5 BFS en matriz

```python
from collections import deque

q = deque()
q.append((start_r, start_c))
visited = set()
visited.add((start_r, start_c))

directions = [(1,0), (-1,0), (0,1), (0,-1)]

while q:
    r, c = q.popleft()

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
            continue

        if (nr, nc) in visited:
            continue

        visited.add((nr, nc))
        q.append((nr, nc))
```

## 33.6 Conteo de frecuencias

```python
count = {}

for x in arr:
    count[x] = count.get(x, 0) + 1
```

## 33.7 Agrupar por clave

Ejemplo: Group Anagrams.

```python
from collections import defaultdict

groups = defaultdict(list)

for word in strs:
    key = tuple(sorted(word))
    groups[key].append(word)

return list(groups.values())
```

Otra forma con conteo de 26 letras:

```python
from collections import defaultdict

groups = defaultdict(list)

for word in strs:
    count = [0] * 26

    for char in word:
        count[ord(char) - ord("a")] += 1

    key = tuple(count)
    groups[key].append(word)

return list(groups.values())
```

¿Por qué `tuple(count)`?

Porque las listas no pueden ser claves de diccionario, pero las tuplas sí.

---

# 34. Mutabilidad: lista vs tupla vs string

## Lista

Mutable. Puedes cambiarla.

```python
nums = [1, 2, 3]
nums[0] = 99
```

Resultado:

```python
[99, 2, 3]
```

## String

Inmutable. No puedes cambiar una posición directamente.

```python
s = "hello"
# s[0] = "H"  # error
```

## Tupla

Inmutable.

```python
point = (1, 2)
```

Las tuplas son útiles como claves de diccionario o elementos de set.

Ejemplo:

```python
visited = set()
visited.add((r, c))
```

No puedes hacer:

```python
visited.add([r, c])  # error
```

Porque las listas son mutables y no pueden ir en un set.

---

# 35. Casos borde que debes probar siempre

Cuando termines una solución, prueba mentalmente:

## Para arrays

```text
[]
[1]
[1, 1]
[1, 2, 3]
números negativos
duplicados
lista ya ordenada
lista en orden inverso
```

## Para strings

```text
""
"a"
"aa"
"ab"
mayúsculas/minúsculas
espacios
símbolos
```

## Para matrices

```text
matriz vacía
1x1
una sola fila
una sola columna
todo agua / todo tierra
bordes
```

## Para linked lists

```text
lista vacía
un nodo
dos nodos
varios nodos
ciclo si aplica
```

## Para trees

```text
árbol vacío
un nodo
solo izquierda
solo derecha
balanceado
desbalanceado
```

---

# 36. Cómo explicar Big O sin trabarte

## Two Sum con hash map

```text
Time complexity is O(n), because I iterate through the array once.
Space complexity is O(n), because in the worst case I store all numbers in the hash map.
```

## Valid Anagram

```text
Time complexity is O(n), because I process each character once.
Space complexity is O(k), where k is the number of distinct characters.
```

Si solo son letras minúsculas:

```text
Since the alphabet size is fixed, the space can be considered O(1).
```

## Sorting

```text
Time complexity is O(n log n), because sorting dominates the algorithm.
```

## Binary Search

```text
Time complexity is O(log n), because each step cuts the search space in half.
Space complexity is O(1), because I only use a few variables.
```

---

# 37. Cómo leer errores de Python comunes

## `IndexError: list index out of range`

Intentaste acceder a un índice que no existe.

```python
nums = [1, 2, 3]
nums[3]  # error
```

Índices válidos:

```text
0, 1, 2
```

## `KeyError`

Intentaste acceder a una clave que no existe en un diccionario.

```python
d = {}
print(d["a"])  # KeyError
```

Soluciones:

```python
if "a" in d:
    print(d["a"])
```

o

```python
d.get("a", 0)
```

## `TypeError: unhashable type: 'list'`

Intentaste usar una lista como clave de dict o elemento de set.

Mal:

```python
seen = set()
seen.add([1, 2])
```

Bien:

```python
seen.add((1, 2))
```

## `AttributeError`

Intentaste usar un método que ese objeto no tiene.

```python
nums = [1, 2, 3]
nums.popleft()  # error
```

`popleft` es de `deque`, no de lista.

Bien:

```python
from collections import deque
q = deque(nums)
q.popleft()
```

---

# 38. Micro chuleta de sintaxis

```python
# loop con índice
for i in range(len(nums)):
    ...

# loop con índice y valor
for i, num in enumerate(nums):
    ...

# loop solo valor
for num in nums:
    ...

# dict
d = {}
d[key] = value
if key in d:
    ...

# set
s = set()
s.add(x)
if x in s:
    ...

# lista como stack
stack = []
stack.append(x)
stack.pop()
stack[-1]

# queue
from collections import deque
q = deque()
q.append(x)
q.popleft()

# heap
import heapq
heapq.heappush(heap, x)
heapq.heappop(heap)

# counter
from collections import Counter
count = Counter(nums)

# defaultdict
from collections import defaultdict
graph = defaultdict(list)

# sorting
nums.sort()
sorted_nums = sorted(nums)
items.sort(key=lambda x: x[1])

# slicing
nums[:k]
nums[k:]
nums[::-1]

# matriz
rows = len(grid)
cols = len(grid[0])
grid[r][c]

# infinito
float("inf")
float("-inf")
```

---

# 39. Mini ejercicios para practicar sintaxis

## Ejercicio 1

Dada una lista, cuenta cuántas veces aparece cada número.

```python
nums = [1, 2, 2, 3, 3, 3]
```

Resultado esperado:

```python
{1: 1, 2: 2, 3: 3}
```

## Ejercicio 2

Dada una lista, regresa `True` si hay duplicados.

```python
nums = [1, 2, 3, 1]
```

Resultado:

```python
True
```

## Ejercicio 3

Dado un string, regresa el string al revés.

```python
s = "hello"
```

Resultado:

```python
"olleh"
```

## Ejercicio 4

Dada una matriz, imprime todos sus valores.

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

Salida:

```text
1
2
3
4
```

## Ejercicio 5

Dada una lista ordenada y un target, implementa binary search.

---

# 40. Mini respuestas

## Respuesta ejercicio 1

```python
count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1
```

## Respuesta ejercicio 2

```python
seen = set()

for num in nums:
    if num in seen:
        return True

    seen.add(num)

return False
```

## Respuesta ejercicio 3

```python
return s[::-1]
```

## Respuesta ejercicio 4

```python
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        print(matrix[r][c])
```

## Respuesta ejercicio 5

```python
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

---

# 41. Mini guía para usar este documento con NotebookLM

Puedes pedirle a NotebookLM:

```text
Hazme flashcards de las secciones de dict, set y deque.
```

```text
Explícame con ejemplos la diferencia entre dict y set.
```

```text
Hazme un quiz de 10 preguntas sobre slicing.
```

```text
Dame 5 ejercicios de matrices y corrígeme mis respuestas.
```

```text
Simula una entrevista técnica usando solo los patrones de este documento.
```

```text
Pregúntame Big O de cada plantilla.
```

```text
Hazme una tabla de errores comunes y cómo evitarlos.
```

```text
Conviértelo en un plan de estudio de 7 días.
```

---

# 42. Regla final

No necesitas memorizar todo Python.

Necesitas dominar estas preguntas:

```text
¿Ya vi este valor? -> set
¿Necesito guardar índice/conteo? -> dict
¿Necesito orden FIFO? -> deque
¿Necesito último en entrar? -> stack
¿Está ordenado? -> binary search / two pointers
¿Es substring/subarray? -> sliding window
¿Es grafo/matriz/árbol? -> BFS/DFS
¿Piden top K? -> heap
```

Si puedes responder eso rápido, ya estás pensando como candidato de entrevista técnica.


