'''
Given an int array wood representing the length of n pieces of wood and an int k.

It is required to cut these pieces of wood such that more or equal to k pieces of
the same length len are cut. What is the longest len you can get?
'''
def isValid(cutLen, A, k):
    cnt = 0
    for wood in A:
        if(wood >= cutLen):
            cnt += wood // cutLen
    return cnt >= k

def cutWood(A, k):
    n = len(A)
    if n == 0:
        return 0
    
    L = 1
    R = max(A)
    current = 1
    while L < R:
        m = L + ((R - L) // 2)
        if isValid(m, A, k):
            current = m
            L = m + 1 # this is valid, so let's check higher cut lengths
        else:
            R = m # cut length too high, so let's drop R down
    
    return current

'''
Input: wood = [232, 124, 456], k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114 long,
however we can't cut it into 7 pieces if any piece is 115 long.
'''
wood = [232, 124, 456]
k = 7
print(cutWood(wood, k))

wood = [10, 6, 5, 3]
k = 4
print(cutWood(wood, k))

wood = [5, 9, 7]
k = 4
print(cutWood(wood, k))
    