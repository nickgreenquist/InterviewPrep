def getVal(M, i, n, m):
    return M[i // m][i % m]

def bs2D(M, L, H, n, m, target):
    if H - L <= 1:
        return getVal(M, L, n, m) == target
    
    mid = L + ((H - L) // 2)
    mid_val = getVal(M, mid, n, m)
    
    if target == mid_val:
        return True
    elif target < mid_val:
        return bs2D(M, L, mid, n, m, target)
    else:
        return bs2D(M, mid, H, n, m, target)
    
def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    return bs2D(matrix, 0, n*m, n, m, target)

matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]

print(searchMatrix(matrix, 34))