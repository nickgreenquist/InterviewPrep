from random import randint

n = 4
mat = []
for i in range(n):
    mat.append( [] )
    for j in range(n):
        mat[i].append(randint(0, 1))

def rotate():
    layers = int(n / 2)
    for layer in range(layers):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = mat[first][i]

            mat[first][i] = mat[last - offset][first]

            mat[last-offset][first] = mat[last][last - offset]

            mat[last][last - offset] = mat[i][last]

            mat[i][last] = top

for row in mat:
    print(row)

rotate()

print("rotated")
for row in mat:
    print(row)


