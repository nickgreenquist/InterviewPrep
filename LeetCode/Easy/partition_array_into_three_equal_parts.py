'''
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with 
(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])
'''

from typing import List
def canThreePartsEqualSum( A: List[int]) -> bool:
    total = sum(A)
    
    # can this even be split into 3 equal chunks
    if total % 3 != 0:
        return False
    
    # init variables we need
    target = total // 3     
    current = 0
    
    # first pass
    i = 0
    while current != target and i < len(A):
        current += A[i]
        i += 1
    if i >= len(A) or current != target:
        return False
    
    # second group
    current = 0
    while current != target and i < len(A):
        current += A[i]
        i += 1
    if i >= len(A) or current != target:
        return False
    
    # final pass - use up the rest
    current = 0
    while i < len(A):
        current += A[i]
        i += 1
    if i != len(A) or current != target:
        return False
    
    return True

'''
Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
'''
print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))

'''
Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
'''
print(canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))