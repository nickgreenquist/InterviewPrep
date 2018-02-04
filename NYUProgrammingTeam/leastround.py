n = int(input())
mat = []
best = []
for i in range(n):
    best.append( [] )
    mat.append( [] )
    row = input()
    row = row.split()
    for j in range(n):
        mat[i].append( int(row[j]) )
        best[i].append(0)

best[0][0] = mat[0][0]
for i in range(1, n):
    mat[0][i] = mat[0][i] * mat[0][i - 1]
    mat[i][0] = mat[i][0] * mat[i - 1][0]

i = 0
j = 0
steps = ""
while i < n - 1 and j < n - 1:
    if mat[i + 1][j] == 1:
        i += 1
        steps +='R'
    elif mat[i][j + 1] == 1:
        j += 1
        steps += 'D'
    elif 10 % (mat[i + 1][j] % 10) != 0:
        i += 1
        steps += 'R'
    elif 10 % (mat[i][j + 1] % 10) != 0:
        j += 1
        steps += 'D'
    else:
        i += 1
        steps += 'R'
while i < n - 1:
    steps += 'R'
    i += 1
while j < n - 1:
    steps += 'D'
    j += 1
    
print(steps)
    

for row in mat:
    print(row)

        