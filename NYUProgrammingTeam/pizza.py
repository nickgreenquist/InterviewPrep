inp = input()
inp = inp.split()
n = int(inp[0])
s = int(inp[1])

mult = []
ones = []
twos = []
for i in range(n):
    inp = input()
    inp = inp.split()
    x = int(inp[0])
    y = int(inp[1])
    z = int(inp[2])

    mult.append(x)
    ones.append(y)
    twos.append(z)

look = []
for i in range(n):
    look.append([])
    for j in range(n):
        look[i].append(0)

happy = 0
use1 = 0
use2 = 0
mark1 = []
mark2 = []
for i in range(n):
    if ones[i] < twos[i]:
        happy += (mult[i] * twos[i])
        use2 = (use2 + mult[i]) % s
        #push
        mark2.append( (twos[i] - ones[i], mult[i]))
    else:
        happy += (mult[i] * ones[i])
        use1 = (use1 + mult[i]) % s
        #push
        mark1.append( (ones[i] - twos[i], mult[i]))



if (use1 + use2) > s:
    print(happy)
sorted(mark1, key=lambda element: (element[0], element[1]))
sorted(mark2, key=lambda element: (element[0], element[1]))
a1 = 0
a2 = 0
i = 0
for tup in mark1:
    #m = min(tup[1], use1)
    #a1 += (m * tup[0])
    m = min(use2, mult[i])
    a1 += (m * (tup[0] - tup[1]))
    use1 -= min(tup[1], use1)
    i += 1

i = 0
for tup in mark2:
    #m = min(tup[1], use2)
    #a2 += (m * tup[0])
    m = min(use2, mult[i])
    a2 += (m * (tup[1] - tup[0]))
    use2 -= min(tup[1], use2)
    i += 1
happy -= min(a1, a2)
print(happy)