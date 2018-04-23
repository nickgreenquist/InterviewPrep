from copy import deepcopy
import random

def sweep(grid, visited, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]):
        return
    if visited[row][col] != '-':
        return 
    visited[row][col] = str(grid[row][col])
    if grid[row][col] == 0:
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                sweep(grid, visited, i, j)

def set_bomb(grid, row, col):
    grid[row][col] = 9
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i]) and grid[i][j] != 9:
                grid[i][j] += 1

def init_grid(width, height, num_bombs):
    bombs = random.sample(range(0, width*height), num_bombs)
    grid = [[0]*width for i in range(height)]
    for bomb in bombs:
        i = bomb // height
        j = int(bomb % width)
        set_bomb(grid, i, j)

    visited = deepcopy(grid)
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            visited[i][j] = '-'
    
    for i in range(len(grid)):
        print(grid[i])

    return grid, visited

def check_win(grid, visited):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if visited[i][j] == '-' and grid[i][j] != 9:
                return False
    return True

def check_lose(grid, visited):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if visited[i][j] != '-' and grid[i][j] == 9:
                return True
    return False

i = int(input("Select height of grid: "))
j = int(input("Select width of grid: "))
b = int(input("Select number of bombs: "))
grid, visited = init_grid(i, j, b)
while True:
    i = int(input("Select row to click: "))
    j = int(input("Select col to click: "))
    sweep(grid, visited, i, j)

    for i in range(len(grid)):
        print(visited[i])

    if check_lose(grid, visited):
        print('YOU LOSE')
        break
    if check_win(grid, visited):
        print("YOU WIN")
        break