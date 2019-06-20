'''
In an N by N square grid, each cell is either empty (0) or blocked (1).

Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
'''

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    
    # check if entrance and exit are blocked off
    if grid[0][0] or grid[n-1][n-1] == 1:
        return -1
    
    # queue will hold triple of (x,y,distance)
    queue = [(0,0,1)]
    
    visited = {}
    
    for i,j,dist in queue:
        if i == n-1 and j == n-1:
            return dist
        
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                # check for standing still
                if x == i and y == j:
                    continue
                    
                if x >= 0 and x < n and y >= 0 and y < n and grid[x][y] == 0 and (x,y) not in visited:
                    queue.append((x,y,dist + 1))
                    visited[(x,y)] = True
    return -1

'''
Input: [[0,0,0],
        [1,1,0],
        [1,1,0]]
Output: 4
'''

grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))