def Insert(n, m, i, j):
    allOnes = ~0
    left = allOnes << (j + 1)
    
    right = ((1 << i) - 1)

    mask = left | right

    n_cleared = n & mask
    m_shifted = m << i

    return m_shifted | n_cleared

n = int('100000000000', 2)
m = int('10011', 2)
m = Insert(n, m, 2, 6)

print( "{0:b}".format(m) )