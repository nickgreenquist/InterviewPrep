'''
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row. 
The next row's choice must be in a column that is different from the previous row's column by at most one.
'''

def minFallingPathSum(A):
    if len(A) == 1:
        return max(A[0])
    
    def traverse(A, row, col, lookup):
        if row >= len(A) or col < 0 or col >= len(A[0]):
            return float('inf')
        
        key = (row, col)
        if row == len(A) - 1:
            return lookup[key]
        
        if key in lookup:
            return lookup[key]
        
        best = float('inf')
        for c in [col - 1, col, col + 1]:
            best = min(best, traverse(A, row + 1, c, lookup))
        lookup[key] = best + A[row][col]
        return lookup[key] 
        
    
    lookup = {}
    for col in range(len(A[0])):
        key = (len(A) - 1, col)
        lookup[key] = A[len(A) - 1][col]
    
    best = float('inf')
    for col in range(len(A[0])):
        best = min(best, traverse(A, 0, col, lookup))
    return best

'''
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
'''
print(minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))