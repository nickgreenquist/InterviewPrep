inp = input().split()
n = int(inp[0])
bx = int(inp[1])

X = input().split()
for i in range(n):
    X[i] = int(X[i])
X = X[::-1]

inp = input().split()
m = int(inp[0])
by = int(inp[1])

Y = input().split()
for i in range(m):
    Y[i] = int(Y[i])
Y = Y[::-1]

sum_X = 0
base = 1
for n in X:
    sum_X += base*n
    base *= bx

sum_Y = 0
base = 1
for n in Y:
    sum_Y += base*n
    base *= by
if sum_X == sum_Y:
    print('=')
elif sum_X < sum_Y:
    print('<')
else:
    print('>')
