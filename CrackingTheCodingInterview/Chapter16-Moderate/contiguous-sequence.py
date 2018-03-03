def cs(array):
    maxsum = 0
    currentsum = 0
    for a in array:
        currentsum += a
        if maxsum < currentsum:
            maxsum = currentsum
        elif currentsum < 0:
            currentsum = 0
    return maxsum

inp = [-8, 3, -2, 4, -10]
inp = [2, 3, -8, -1, 2, 4, -2, 3]
sum = cs(inp)
print(sum)