def minProduct(x, y):
    bigger = max(x, y)
    smaller = min(x, y)
    return minProductHelper(smaller, bigger)

def minProductHelper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller ==  1:
        return bigger

    s = smaller >> 1 #shift right 1, same as divide by 2
    halfProd = minProductHelper(s, bigger)

    #if smaller shifted to the right 1 and then back is the same numbe,
    #we know it is divisible by 2
    if (((smaller >> 1) << 1) == smaller):
        return halfProd + halfProd
    else:
        return halfProd + halfProd + bigger

print (minProduct(5,100) )