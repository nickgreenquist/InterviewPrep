from random import randint

n = 3
mat = []
for i in range(n):
    mat.append( [] )
    for j in range(n):
        mat[i].append( randint(1,1))
mat[0][0] = 0



def zero():
    zrows = []
    zcols = []
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                zrows.append(i)
                zcols.append(j)
    
    for zrow in zrows:
        for i in range(n):
            mat[zrow][i] = 0
    for zcol in zcols:
        for i in range(n):
            mat[i][zcol] = 0

for row in mat:
    print(row)

zero()
print()
for row in mat:
    print(row)