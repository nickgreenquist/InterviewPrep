n = int(input())

p1 = ""
p1s = 0
p2 = ""
p2s = 0

r = input()
p = r.split()[0]
s = r.split()[1]

p1 = p
p1s += int(s)

win = p1

for i in range(1, n):
    r = input()
    p = r.split()[0]
    s = r.split()[1]
    
    if p == p1:
        p1s += int(s)
    else:
        p2 = p
        p2s += int(s)

    if p1s < 0:
        print(p2)
        break
    if p2s < 0:
        print(p1)
        break
    
    if p1s > p2s:
        win = p1
    if p2s > p1s:
        win = p2

if p1s > p2s:
    print(p1)
if p2s > p1s:
    print(p2)
if p1s == p2s:
    print(win)

    