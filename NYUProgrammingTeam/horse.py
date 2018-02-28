inp = input()
inp = inp.split()
n = int(inp[0])
m = int(inp[1])
k = int(inp[2])

a = []
inp = input().split()
for i in inp:
    a.append(int(i))

mind = 1000000000000000
dist = 0
for i in range(m, n):
    dist += 10
    if a[i] <= k and a[i] != 0:
        mind = dist
        break
dist = 0
for i in range(m-2, -1, -1):
    dist += 10
    if a[i] <= k and a[i] != 0:
        if dist >= mind:
            break
        if dist < mind:
            mind = dist
            break

print(mind)