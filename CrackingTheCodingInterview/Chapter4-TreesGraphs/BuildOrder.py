import queue

# Topological Sort
def BuildOrder(projects, depend):
    neighbors = {}
    blockers = {}
    for p in projects:
        neighbors[p] = []
        blockers[p] = 0

    for pair in depend:
        neighbors[pair[0]].append(pair[1])
        blockers[pair[1]] += 1
    
    q = queue.Queue()
    for key,value in blockers.items():
        if value == 0:
            q.put(key)
    
    while not q.empty():
        p = q.get()
        print(p)

        for neighbor in neighbors[p]:
            blockers[neighbor] -= 1
            if blockers[neighbor] <= 0:
                q.put(neighbor)


projects = ['a', 'b', 'c', 'd', 'e', 'f']
depend = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
BuildOrder(projects, depend)
