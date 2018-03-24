inp = input().split()

n = int(inp[0])
m = int(inp[1])

ans = 0
l = 0
r = 2000000000
n -= m
while l <= r:
    mid = (l + r) // 2
    if (mid * (mid + 1)) / 2 < n:
        l = mid + 1
    else:
        r = mid - 1
        ans = mid

print(ans + m)
