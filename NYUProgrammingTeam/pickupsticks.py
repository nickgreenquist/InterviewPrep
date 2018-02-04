

inp = input()
inp = inp.split()

n = int(inp[0])
m = int(inp[1])

order = []
h = {}

for i in range(0, m):
    order.append(0)
    order.append(0)
    inp = input()
    inp = inp.split()

    a = int(inp[0])
    b = int(inp[1])
    
    if a not in h:
        h[a] = 0
    if b not in h:
        h[b] = 0
    h[b] = h[a] + 1
for k,v in h.items():
    order[v] = k

blah = input()

for i in range(0, n):
    print(order[i])
                


