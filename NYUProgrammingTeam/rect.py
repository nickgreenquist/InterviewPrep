dim = input()
n = int(dim.split()[0])
m = int(dim.split()[1])

bad = ""
for i in range(0, m):
    bad += "."

drawing = []
left = 10000000
right = -10000000

addtop = True
top = 0
bottom = n
for i in range(0, n):
    row = input()

    if addtop:
        if row == bad:
            top += 1
        else:
            addtop = False

    

    #update left offset
    lo = 0
    for c in row:
        if c == '*':
            break
        lo += 1
    if lo < left:
        left = lo

    #update right offset
    ro = len(row)
    for i in range(len(row) - 1, -1, -1):
        if row[i] == '*':
            break
        ro -= 1
    if ro > right:
        right = ro

    drawing.append(row)

for i in range(n - 1, 0, -1):
    if drawing[i] == bad:
        bottom -= 1
    else:
        break

drawing = drawing[top:bottom]
for i in range(0, len(drawing)):
    drawing[i] = drawing[i][left:right]
    print(drawing[i])


