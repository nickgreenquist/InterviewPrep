i  = input().split()
n = int(i[0])
m = int(i[1])

a = input().split()
for i in range(0, n):
    a[i] = int(a[i])

ms = []
max_m = 0
for i in range(0, m):
    num = int(input())
    ms.append(num)
    if max_m < num:
        max_m = num


u = {}
seen = {}
count = 0
for i in range(max_m-1, -1, -1):
    if a[i] not in seen:
        count += 1
        seen[a[i]] = True
    u[i] = count

for i in range(0, m):
    a = ms[i]
    print(u[a-1])