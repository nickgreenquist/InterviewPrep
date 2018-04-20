def rotate_in_place(grid):
    top = 0
    bottom = len(grid) - 1
    left = 0
    right = len(grid[0]) - 1

    max_offset = len(grid) - 1
    while left < right and top < bottom:
        for offset in range(0, max_offset):
            # 1. Top left to top right
            prev = grid[top][right - offset]
            grid[top][right - offset] = grid[top + offset][left]

            # 2. Top right to bottom right
            curr = grid[bottom - offset][right]
            grid[bottom - offset][right] = prev
            prev = curr

            # 3. Bottom right to bottom left
            curr = grid[bottom][left + offset]
            grid[bottom][left + offset] = prev
            prev = curr

            # 4. Bottom left to top left
            grid[top + offset][left] = prev

            for row in grid:
                print(row)
            print()
        top += 1
        bottom -= 1
        left += 1
        right -= 1
        max_offset -= 2
    return grid
        
grid = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

grid = rotate_in_place(grid)
for row in grid:
    print(row)