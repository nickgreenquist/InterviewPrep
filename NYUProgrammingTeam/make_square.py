import math
s = input()

n = len(s)

ans = -1

num = ''

for i in range(1, 1 << n):
    st = ''
    for j in range(n):
        if i >> j & 1:
            st += s[j]
    
    if st[0] != '0':
        temp = int(st)
        
        k = int(math.sqrt(temp))

        if k * k == temp:
            if ans < int(len(st)):
                ans = int(len(st))
                num = st

if ans == -1:
    print(ans)
else:
    print(n-ans)

