
def comp(x):
    return x[1] * x[2]

n = 100000
case = 1
while(n != 0):
    n = int(input())
    if n == 0:
        break
    blocks = []
    for i in range(n):
        b = input().split()

        h = int(b[0])
        d = int(b[1])
        w = int(b[2])

        blocks.append( (h, max(w,d), min(w,d)) )
        blocks.append( (w, max(h, d), min(h, d)) )
        blocks.append( (d, max(h, w), min(h, w)) )

    n *= 3
    blocks = sorted(blocks, key=lambda x: -comp(x) )

    msh = [0] * n
    for i in range(n):
        msh[i] = blocks[i][0]

    for i in range(1, n):
        msh[i] = 0
        val = 0
        for j in range(0, i):
            if blocks[i][2] < blocks[j][2] and blocks[i][1] < blocks[j][1]:
                val = max(val, msh[j])
        msh[i] = val + blocks[i][0]
    maxx = -1
    for i in range(n):
        if maxx < msh[i]:
            maxx = msh[i]
    print("Case %s: maximum height = %s" % (case, maxx))
    case += 1



'''
1
10 20 30
2
6 8 10
5 5 5
7
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
5
31 41 59
26 53 58
97 93 23
84 62 64
33 83 27
0
'''