
def fourSumCount(A, B, C, D):
    lookup = {}
    for a in A:
        for b in B:
            goal = a + b
            if goal in lookup:
                lookup[goal] += 1
            else:
                lookup[goal] = 1
    tuples = 0
    for c in C:
        for d in D:
            target = -(c + d)
            if target in lookup:
                tuples += lookup[target]
    return tuples

# Input
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
'''
Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''
print(fourSumCount(A, B, C, D))