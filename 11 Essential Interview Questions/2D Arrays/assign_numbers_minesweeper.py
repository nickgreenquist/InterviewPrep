def assign(grid, r, c):
    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
        if grid[r][c] != -1:
            grid[r][c] += 1

def mine_sweeper(bombs, num_rows, num_cols):
    grid = [ [0] * num_cols for i in range(num_rows)]
    for bomb in bombs:
        r = bomb[0]
        c = bomb[1]
        
        # assign top 3
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                assign(grid, i, j)
        grid[r][c] = -1

    return grid

grid = mine_sweeper([[0,0], [0,1]], 3, 4)
for row in grid:
    print(row)
