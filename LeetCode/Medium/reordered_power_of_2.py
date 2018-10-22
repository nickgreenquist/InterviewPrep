'''
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.
Return true if and only if we can do this in a way such that the resulting number is a power of 2.
'''

def reorderedPowerOf2(N):
    count = {}
    for c in str(N):
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    
    for i in range(30):
        pow_count = {}
        for c in str(pow(2,i)):
            if c in pow_count:
                pow_count[c] += 1
            else:
                pow_count[c] = 1
        if pow_count == count:
            return True
    return False