i = input()
i = i.split()
n = int(i[0])
m = int(i[1])

a = min(n,m)
b = max(n,m)

i = 5
ans = 0
while i <= n + m:
    if i <= a:
        ans += i - 1
    elif i > a and i <= b:
        ans += a
    else:
        ans += (a - i + b + 1)
    i += 5
print(ans)