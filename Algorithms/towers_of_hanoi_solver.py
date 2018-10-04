A = []
B = []
C = []

def printPoles():
    global A, B, C
    print("A={}, B={}, C={}".format(A, B, C))

def moveDisk(src, target):
    n = src.pop(0)
    target.insert(0, n)
    printPoles()

def TOH(n, src, target, spare):
    if n == 1:
        moveDisk(src, target)
    else:
        TOH(n-1, src, spare, target)
        moveDisk(src, target)
        TOH(n-1, spare, target, src)

num_disks = 4
for i in range(1, 4+1):
    A.append(i)
printPoles()

#use the solver
TOH(len(A), A, B, C)