'''
Write methods to implement the multiply, subtract, and divide operations for integers. 
The results of all of these are integers. Use only the add operator
'''

def negate(a):
    temp = 0
    i = 1
    if a > 0:
        i = -1
    while a != 0:
        a += i
        temp += i
    return temp

def subtract(a, b):
    return a + negate(b)

def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    absa = abs(a)
    absb = abs(b)
    product = 0
    for i in range(absa):
        product += absb
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return product
    return negate(product)

def divide(a, b):
    if b == 0:
        return None
    if a == 0:
        return 0
    absa = abs(a)
    absb = abs(b)
    result = 0
    temp = absb
    while temp <= absa:
        result += 1
        temp += absb
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return result
    return negate(result)


print(divide(13, 7))