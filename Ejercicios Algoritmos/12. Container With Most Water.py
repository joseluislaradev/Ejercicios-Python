# Problema principal: Container With Most Water

# Container → /kənˈteɪ.nər/ → contenedor.

# Recibes una lista donde cada número representa la altura de una línea vertical:

# heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Debes escoger dos líneas para formar un contenedor que guarde la mayor cantidad de agua posible.

# Cómo se calcula el área

# Para dos índices left y right:

# ancho  = right - left
# altura = la menor de las dos alturas
# área   = ancho × altura

# En código:

# width = right - left
# height = min(heights[left], heights[right])
# area = width * height

# Usamos la menor altura porque el agua se derramaría por ese lado.

# Ejemplo
# heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# La mejor pareja es:

# índice 1: altura 8
# índice 8: altura 7

# Entonces:

# ancho = 8 - 1 = 7
# altura útil = min(8, 7) = 7

# área = 7 × 7 = 49

# Resultado:

# 49

def max_water_container(heights):
    left = 0
    right = len(heights) - 1
    max_area = 0
    area = 0
    width = 0
    height = 0
    
    
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        
        max_area = max(max_area, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
            
    return max_area
            
        
    


print(max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# 49

print(max_water_container([1, 1]))
# 1

print(max_water_container([4, 3, 2, 1, 4]))
# 16

print(max_water_container([1, 2, 1]))
# 2

print(max_water_container([]))
# 0

print(max_water_container([5]))
# 0