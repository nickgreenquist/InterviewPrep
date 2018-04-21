import sys
import math

def length(x):
    x = str(x)
    return len(x)

inp = input().split()
m = int(inp[0])
s = int(inp[1])

if s == 0 and m == 1:
    print('0 0')
elif s < 1 or s > 9 * m:
    print('-1 -1')
else:
    digits = [0 for i in range(m)]
    nines = s // 9
    remain = int(s % 9)

    for i in range(0, m - nines):
        digits[i] = 0
    for i in range(m - nines, m):
        digits[i] = 9
    
    i = m - nines
    if remain > 0:
        i -= 1
        digits[i] = remain
    if digits[0] == 0:
        digits[0] += 1
        digits[i] -=1
    for i in range(m):
        print(digits[i], end='', flush=True)
    print(' ', end='')
    
    for i in range(nines):
        digits[i] = 9
    for i in range(nines, m):
        digits[i] = 0
    if remain > 0:
        digits[nines] = remain
    for i in range(m):
        print(digits[i], end='', flush=True)
