'''
This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.

Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?
'''

def traverse(i, j, N, lookup, m):
    if (i < 0 or j < 0 or i >= 4 or j >= 3 or (i == 3 and j != 1)):
        return 0
    if N == 1:
        return 1
    if lookup[N][i][j] > 0:
        return lookup[N][i][j]
    
    lookup[N][i][j] = traverse(i-2, j-1, N-1, lookup, m) % m + traverse(i-2, j+1, N-1, lookup, m) % m + traverse(i-1, j-2, N-1, lookup, m) % m + traverse(i-1, j+2, N-1, lookup, m) % m + traverse(i+1, j-2, N-1, lookup, m) % m + traverse(i+1, j+2, N-1, lookup, m) % m + traverse(i+2, j-1, N-1, lookup, m) % m + traverse(i+2, j+1, N-1, lookup, m) % m
    return int(lookup[N][i][j])

def knightDialer(N):
    count = 0
    lookup = [[[0 for k in range(3)] for j in range(4)] for i in range(N+1)]
    m = (pow(10,9) + 7)
    for i in range(4):
        for j in range(3):
            count = (count + traverse(i, j, N, lookup, m)) % m
    return count % m

'''
Input: 3
Output: 46
'''
print(knightDialer(3))