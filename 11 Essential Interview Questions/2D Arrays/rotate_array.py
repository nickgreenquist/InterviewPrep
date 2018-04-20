def rotate(grid):
    new_grid = [ [0] * len(grid[0]) for i in range(len(grid))]
    layers = []
    for row in grid:
        layers.append(row)

    layers = layers[::-1]
    for col in range(len(grid[0]) -1, -1, -1):
        layer = layers[col]
        for row in range(0, len(grid)):
            new_grid[row][col] = layer[row]
    return new_grid

def rotate_better(grid):
    new_grid = [ [0] * len(grid[0]) for i in range(len(grid))]
    length = len(grid)
    for i in range(length):
        for j in range(length):
            new_grid[j][length - i - 1] = grid[i][j]
    return new_grid

grid = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
grid = rotate_better(grid)
for row in grid:
    print(row)

