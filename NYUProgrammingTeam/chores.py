inp = input()
inp = inp.split()
n = int(inp[0])
k = int(inp[1])
x = int(inp[2])

chores = input().split()
ans = 0
for i in range(n):
    a = int(chores[i])
    if i < n - k:
        ans += a
    else:
        ans += x
print(ans)


