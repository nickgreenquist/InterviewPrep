'''
You have an integer matrix representing a plot of land, where the value at that location represents the height above sea level. 
A value of zero indicates water. A pond is a region of water connected vertically, horizontally, or diagonally. 
The size of the pond is the total number of connected water cells. Write a method to compute the sizes of all ponds in the matrix
'''

'''
Input:
0 2 1 0 
0 1 0 1 
1 1 0 1 
0 1 0 1
Output: 2, 4, 1 (in any order)
'''

def explore_pond(terrain, i, j, seen):
    if (i < 0 or 
        j < 0 or 
        i >= len(terrain) or
        j >= len(terrain) or 
        (i,j) in seen or
        terrain[i][j] != 0):
        return 0
    size = 1
    seen.add((i,j))
    for k in range(i - 1, i + 2):
        for m in range(j - 1, j + 2):
            size += explore_pond(terrain, k, m, seen)
    return size
    

def pond_sizes(terrain):
    sizes = []
    seen = set()

    for i in range(len(terrain)):
        for j in range(len(terrain[i])):
            if (i,j) not in seen and terrain[i][j] == 0:
                sizes.append(explore_pond(terrain, i, j, seen))
    return sizes


terrain = [
    [0,2,1,0],
    [0,1,0,1],
    [1,1,0,1],
    [0,1,0,1]
]
print(pond_sizes(terrain))