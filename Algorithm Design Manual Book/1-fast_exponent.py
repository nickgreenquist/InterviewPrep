'''
Write a function to perform x^y
'''

def fast_exp(x, y):
    if y == 1:
        return x
    if y == 0:
        return 1

    # O(logn) time since halving y repeatedly
    res = fast_exp(x, y//2)
    
    if y % 2 == 0:
        return res * res
    else:
        return x * res * res


print(fast_exp(5, 3))




    