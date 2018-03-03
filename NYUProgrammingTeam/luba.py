inp = input()
inp = str(inp)
a = [0] * 6
ticket = []
for c in inp:
    ticket.append(int(c))
sum1 = 0
sum2 = 0
for i in range(3):
    sum1 += ticket[i]
    a[i] = ticket[i]
for i in range(3, 6):
    sum2 += ticket[i]
    a[i] = ticket[i]

sum3 = sum1 - sum2
if sum3 > 0:
    for i in range(3, 6):
        a[i] = 9 - a[i]
else:
    for i in range(3):
        a[i] = 9 - a[i]
    sum3 = -sum3

a = sorted(a)
printed = False
for i in range(5, 1, -1):
    if sum3 <= 0:
        print(5-i)
        printed = True
        break
    sum3 -= a[i]
if not printed:
    print(0)