avail = [1,2,3]
buffer = []

def PermAll(k):
    if k == 0:
        print(buffer)
    else:
        for i in range(0, k):
            buffer.append(avail[i])
            PermAll(k-1)
            buffer.remove(avail[i])


avail = [1,2,3]
buffer = []
PermAll(len(avail))