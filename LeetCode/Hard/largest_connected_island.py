class IslandFinder(object):
    def __init__(self):
        self.next_island = 0
        
    def largestIsland(self, grid):
        def traverse(i, j, grid, seen, island):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            if (i,j) in seen:
                return 0
            
            island[i][j] = self.next_island
            seen.add((i,j))
            size = 1
            size += traverse(i + 1, j, grid, seen, island)
            size += traverse(i - 1, j, grid, seen, island)
            size += traverse(i, j + 1, grid, seen, island)
            size += traverse(i, j - 1, grid, seen, island)
            return size
        
        rows = len(grid)
        cols = len(grid[0])
        island_size = {}
        seen = set()
        island = [[None]*cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and island[i][j] is None:
                    size = traverse(i, j, grid, seen, island)
                    island_size[self.next_island] = size
                    self.next_island += 1
        
        # set best size for each cell by which island they belong to
        best = [[0]*cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if island[i][j] is not None:
                    best[i][j] = island_size[island[i][j]]
        
        # go through each cell and if zero, check surrounding neighbors for best chain
        best_chain = float('-inf')
        
        for k,v in island_size.items():
            best_chain = max(best_chain, v)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    best_chain = max(best_chain, 1)
                    
                    '''
                    Singles
                    '''
                    # north
                    if i - 1 >= 0:
                        best_chain = max(best_chain, 1 + best[i-1][j])
                    
                    # east
                    if j + 1 < cols:
                        best_chain = max(best_chain, 1 + best[i][j+1])
                    
                    # south
                    if i + 1 < rows:
                        best_chain = max(best_chain, 1 + best[i+1][j])
                    
                    # west
                    if j - 1 >= 0:
                        best_chain = max(best_chain, 1 + best[i][j-1])
                    
                    '''
                    Doubles
                    '''
                    # north and east
                    if i - 1 >= 0 and j + 1 < cols and island[i-1][j] != island[i][j+1]:
                        best_chain = max(best_chain, 1 + best[i-1][j] + best[i][j+1])
                    
                    # north and south
                    if i - 1 >= 0 and i + 1 < cols and island[i-1][j] != island[i+1][j]:
                        best_chain = max(best_chain, 1 + best[i-1][j] + best[i+1][j])
                    
                    # north and west
                    if i - 1 >= 0 and j - 1 < cols and island[i-1][j] != island[i][j-1]:
                        best_chain = max(best_chain, 1 + best[i-1][j] + best[i][j-1])
                    
                    # east and south
                    if i + 1 < rows and j + 1 < cols and island[i+1][j] != island[i][j+1]:
                        best_chain = max(best_chain, 1 + best[i+1][j] + best[i][j+1])
                    
                    # east and west
                    if j + 1 <cols and j - 1 >= 0 and island[i][j+1] != island[i][j-1]:
                        best_chain = max(best_chain, 1 + best[i][j+1] + best[i][j-1])
                    
                    # south and west
                    if i + 1 < rows and j - 1 >= 0 and island[i+1][j] != island[i][j-1]:
                        best_chain = max(best_chain, 1 + best[i+1][j] + best[i][j-1])
                        
                    '''
                    Triples
                    '''
                    # north and east and south
                    if i - 1 >= 0 and j + 1 < cols and i + 1 < rows and len(set([island[i-1][j], island[i][j+1], island[i+1][j]])) == 3:
                        best_chain = max(best_chain, 1 + best[i-1][j] + best[i][j+1] + best[i+1][j])
                    
                    # north and south and west
                    if i - 1 >= 0 and i + 1 < rows and j - 1 >= 0 and len(set([island[i-1][j], island[i+1][j], island[i][j-1]])) == 3:
                        best_chain = max(best_chain, 1 + best[i-1][j] + best[i+1][j] + best[i][j-1])
                    
                    # east and south and west
                    if j + 1 < cols and i + 1 < rows and j - 1 >= 0 and len(set([island[i][j+1], island[i+1][j], island[i][j-1]])) == 3:
                        best_chain = max(best_chain, 1 + best[i][j+1] + best[i+1][j] + best[i][j-1])
                    
                    '''
                    All 4
                    '''
                    if i + 1 < rows and i - 1 >= 0 and j + 1 < cols and j - 1 >= 0 and len(set([island[i+1][j], island[i-1][j], island[i][j+1], island[i][j-1]])) == 4:
                        best_chain = max(best_chain, 1 + best[i][j+1] + best[i+1][j] + best[i][j-1] + best[i-1][j])
        return best_chain
        

# Input    
grid = [
    [0,1,0],
    [1,0,1],
    [0,1,0]
]
# Expected: 5
# Explanation: setting middle 0 to 1 connects the 4 islands

solver = IslandFinder()
print(solver.largestIsland(grid))