def updateVal(matrix, areas, i, j):
    if i == 0 or j == 0:
        areas[i][j] = 1
        return
    
    mv = areas[i-1][j]
    for x,y in [(i-1, j), (i-1, j-1), (i, j-1)]:
        mv = min(mv, areas[x][y])
    areas[i][j] = mv + 1
    
def maximalSquare(matrix):
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    areas = [[0] * n for i in range(m)]
    best = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                updateVal(matrix, areas, i, j)
                best = max(best, areas[i][j])
    return best * best
'''
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''
print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))