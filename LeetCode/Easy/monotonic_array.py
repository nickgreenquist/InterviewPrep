def isMonotonic(A):
    is_minc = True
    is_mdec = True
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            is_minc = False
            break
    for i in range(len(A)-2, -1, -1):
        if A[i] < A[i+1]:
            is_mdec = False
            break
    return is_minc or is_mdec
'''
Input: [1,2,2,3]
Output: true

Input: [6,5,4,4]
Output: true
'''
print(isMonotonic([1,2,2,3]))
print(isMonotonic([6,5,4,4]))