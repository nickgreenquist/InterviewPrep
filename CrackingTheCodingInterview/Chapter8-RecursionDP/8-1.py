memo = {}

def TripleStep(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        if n in memo:
            return memo[n]
        memo[n] =  TripleStep(n-1) + TripleStep(n-2) + TripleStep(n-3)
        return memo[n]

print( TripleStep(37) )