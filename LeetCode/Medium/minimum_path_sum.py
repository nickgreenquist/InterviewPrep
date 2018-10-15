'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

def minPathSum(grid):
    N = len(grid)
    M = len(grid[0])
    for i in range(1, N):
        grid[i][0] += grid[i-1][0]
    for j in range(1, M):
        grid[0][j] += grid[0][j-1]
    
    for i in range(1, N):
        for j in range(1, M):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    return grid[N-1][M-1]

'''
Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

print(minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))