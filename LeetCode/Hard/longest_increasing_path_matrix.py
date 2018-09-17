'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed)
'''
def traverse(matrix, i, j, longest):
    if longest[i][j] == 0: # not seen yet
        val = matrix[i][j]
        best = 0
        for tup in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
            i2 = tup[0]
            j2 = tup[1]
            if i2 >= 0 and j2 >= 0 and i2 < len(matrix) and j2 < len(matrix[0]) and val > matrix[i2][j2]:
                best = max(best, traverse(matrix, i2, j2, longest))
        
        # best path from here is best path from any valid neighbor + 1
        longest[i][j] = best + 1
    return longest[i][j]

    
def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    longest = [[0] * cols for i in range(rows)]
    return max(traverse(matrix, i, j, longest) for i in range(rows) for j in range(cols))

nums =  [
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
'''
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
'''
print(longestIncreasingPath(nums))
                