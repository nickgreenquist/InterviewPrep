def is_rotation(A, B):
    if len(A) != len(B):
        return False
    # Find the element in B that matches first in A
    j = 0
    while B[j] != A[0] and j < len(B):
        j += 1
    
    if B[j] != A[0]:
        return False
    
    for i in range(len(A)):
        if A[i] != B[j]:
            return False
        j += 1
        if j >= len(B):
            j = 0
    return True

A = [1,2,3,4,5,6,7]
B = [4,5,6,7,1,2,3]
print(is_rotation(A, B))