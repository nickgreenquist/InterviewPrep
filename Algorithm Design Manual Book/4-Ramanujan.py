import math

def isRamanujan(num):
    # get cube_root
    L = int(math.pow(num, 1/3)) + 1
    
    pairs = []
    for i in range(1, L):
        for j in range(1, L):
            pairs.append((i, j))
    
    valid_pairs = set()
    for pair in pairs:
        i = pair[0]
        j = pair[1]
        if i**3 + j**3 == num:
            valid_pairs.add(tuple(sorted((i, j))))
    
    print(valid_pairs)

num = 1729
isRamanujan(num)
