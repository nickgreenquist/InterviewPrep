def guess(n, pick):
    if n == pick:
        return 0
    elif n > pick:
        return 1
    else:
        return -1

def binarysearch(L, H, pick):
    if L >= H:
        return L
    
    m = L + ((H - L) // 2)
    g = guess(m, pick)
    if g == 0:
        return m
    elif g == 1:
        return binarysearch(m, H, pick)
    else:
        return binarysearch(L, m, pick)
    
def guessNumber(n, pick):
    return binarysearch(1, n+1, pick)

'''
Input: n = 10, pick = 6
Output: 6
'''

n = 10
pick = 6
print(guessNumber(n, pick))