def check():
    n = input()
    n = n.split()
    for i in range(len(n)):
        n[i] = int(n[i])

    seg = False
    for i in range(len(n)):
        for k in range(i + 1, len(n)):
            for p in range(k + 1, len(n)):
                l1 = n[i]
                l2 = n[k]
                l3 = n[p]

                if l2 + l3 > l1 and l1 + l3 > l2 and l1 + l2 > l3:
                    return 'TRIANGLE'
                if l2 + l3 == l1 or l1 + l3 == l2 or l1 + l2 == l3:
                    seg = True
    if seg:
        return 'SEGMENT'
    return 'IMPOSSIBLE'
print (check())




