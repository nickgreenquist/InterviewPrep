def sqrt(x):
    '''
        Newton's Method
    '''
    if x < 0:
        return None
    elif x == 0:
        return 0
    else:
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r

def sqrt2(x):
    '''
        Binary Search
    '''
    if x < 0:
        return None
    if x >= 1:
        low = 1
        high = x
    else:
        low = 0
        high = 1
    mid = (low + high) / 2
    old_mid = 2*x
    while mid*mid != x and old_mid != mid:
        if mid*mid < x:
            low = mid
        else:
            high = mid

        old_mid = mid
        mid = (low + high) / 2
    return mid

x = 8
print("Newton's Method: sqrt({})={}".format(x, sqrt(x)))
print("Binary Search:   sqrt({})={}".format(x, sqrt2(x)))