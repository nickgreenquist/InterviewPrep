moves = ""

def SolveGrid(grid, i, j, r, c):
    global moves
    if i == (r-1) and j == (c-1):
        return True
    if i >= r:
        return False
    if j >= c:
        return False
    if grid[i][j] == 'X':
        return False

    if SolveGrid(grid, i, j + 1, r, c):
        moves += 'R'
        return True
    if SolveGrid(grid, i + 1, j, r, c):
        moves += 'D'
        return True
    return False

grid = [
    ['O', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', ' ']
]
SolveGrid(grid, 0, 0, len(grid), len(grid[0]))
print(moves[::-1])