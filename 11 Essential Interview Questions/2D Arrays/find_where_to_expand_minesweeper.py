def reveal(grid, r, c):
    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
        if grid[r][c] == 0:
            grid[r][c] = -2
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    reveal(grid, i, j)
    return grid



grid = [
    [-1,1,0,0],
    [1,1,0,0],
    [0,0,1,1],
    [0,0,1,-1]
]
grid = reveal(grid, 0, 2)
for row in grid:
    print(row)
print()

grid = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,1,-1,1,0]
]
grid = reveal(grid, 0, 2)
for row in grid:
    print(row)