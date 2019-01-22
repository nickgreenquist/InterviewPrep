'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number,
also in sorted non-decreasing order.
'''

def sortedSquares(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    
    B = [0 for i in range(len(A))]
    k = len(B) - 1
    
    i = 0
    j = len(A) - 1
    while i <= j:
        low = abs(A[i])
        hi = abs(A[j])
        if low > hi:
            B[k] = low**2
            i += 1
        else:
            B[k] = hi**2
            j -= 1
        k -= 1

    return B

print(sortedSquares([-4,-1,0,3,10]))
# Output: [0,1,9,16,100]

print(sortedSquares([-7,-3,2,3,11]))
# Output: [4,9,9,49,121]