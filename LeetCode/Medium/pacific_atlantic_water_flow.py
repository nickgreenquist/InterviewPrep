def pacificAtlantic(heights):
    rows = len(heights)
    cols = len(heights[0])

    pacific = set()
    atlantic = set()

    def DFS(r, c, visited, prevHeight):
        if r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prevHeight or (r,c) in visited:
            return
        
        visited.add((r,c))
        DFS(r+1, c, visited, heights[r][c])
        DFS(r-1, c, visited, heights[r][c])
        DFS(r, c+1, visited, heights[r][c])
        DFS(r, c-1, visited, heights[r][c])

    # start DFS from top row and bottom row
    for c in range(0, cols):
        DFS(0, c, pacific, heights[0][c])
        DFS(rows-1, c, atlantic, heights[rows-1][c])
    
    # start DFS from left col and right col
    for r in range(0, rows):
        DFS(r, 0, pacific, heights[r][0])
        DFS(r, cols-1, atlantic, heights[r][cols-1])

    ans = []
    for r in range(rows):
        for c in range(cols):
            if (r,c) in atlantic and (r,c) in pacific:
                ans.append([r,c])
    return ans


'''
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
'''

# heights = [[10,10,10],[10,1,10],[10,10,10]]
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
ans = pacificAtlantic(heights)
print(ans)