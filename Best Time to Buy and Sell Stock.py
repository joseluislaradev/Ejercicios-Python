# You are given an array prices where prices[i] is the price of a stock on the i th day.

# You want to maximize your profit by choosing one day to buy and a different later day to sell.

# Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.

# Ejemplo:

# prices = [7, 1, 5, 3, 6, 4]

# Resultado:

# 5

# Porque compras en 1 y vendes después en 6.

# Otro:

# prices = [7, 6, 4, 3, 1]

# Resultado:

# 0


# def profitDays(prices):
    
#     minimum = prices[0]
#     maximum = 0
#     result = 0
    
#     for price in prices:
#         if price < minimum:
#             minimum = price
#             maximum = price
#             continue
        
#         if (price > maximum):
#             maximum = price
            
#         result = max(result, maximum - minimum)

#     print(result)
    
    
# profitDays([1,2])



# prices = [7, 1, 5, 3, 6, 4]

def profitDays(prices):
    
    minimum = prices[0]
    result = 0
    
    for price in prices:
        if price <= minimum:
            minimum = price
        
        result = max(result, price - minimum)

    return result
    
    
profitDays([7, 6, 4, 3, 1])