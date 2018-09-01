def climb(lookup, n):
    if n in lookup:
        return lookup[n]
    lookup[n] = climb(lookup, n-1) + climb(lookup, n-2)
    return lookup[n]
    
def climbStairs(n):
    lookup = {0: 0, 1: 1, 2: 2}
    return climb(lookup, n)

print(climbStairs(5))