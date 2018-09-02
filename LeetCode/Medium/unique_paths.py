'''
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right


Input: m = 7, n = 3
Output: 28
'''
def search(i, j, m, n, lookup):
    if i >= n:
        return 0
    if j >= m:
        return 0
    if i == n-1 and j == m-1:
        return 1
    key = 'i:' + str(i) + ',j:' + str(j)
    if key in lookup:
        return lookup[key]
    lookup[key] = search(i+1, j, m, n, lookup) + search(i, j+1, m, n, lookup)
    return lookup[key]

def uniquePaths(m, n):
    lookup = {}
    return search(0,0,m,n,lookup)

print("m=3, n=2: {}".format(uniquePaths(3, 2)))
print("m=7, n=3: {}".format(uniquePaths(7, 3)))