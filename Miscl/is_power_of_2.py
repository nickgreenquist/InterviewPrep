def isPowerOfTwoBitwise(x):
    # binary representation of (x-1) can be obtained by simply flipping
    # all the bits to the right of rightmost 1 in x
    # and also including the rightmost 1.

    # Now think about x & (x-1). x & (x-1) will have all the bits 
    # equal to the x except for the rightmost 1 in x.
    if x == 0:
        return 
    
    # if all values are 0, the number was power of 2
    return not (x & (x-1))
    

def isPowerOfTwo(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n = n / 2
    if n == 1:
        return True
    return False

print(isPowerOfTwo(6))
print(isPowerOfTwo(8))

print(isPowerOfTwoBitwise(6))
print(isPowerOfTwoBitwise(8))
