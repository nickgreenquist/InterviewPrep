def dfs(graph, v, state, parent_discovered, cycles):
    state[v] = 1 # SEEN

    for u in graph[v]:
        if state[u] == 2: # PROCESSED
            continue
        elif state[u] == 1: # SEEN
            parent_discovered[u] = v
            cycles.add(u)
            break
        else:
            parent_discovered[u] = v
            dfs(graph, u, state, parent_discovered, cycles)

    state[v] = 2 # PROCESSED

def detectCycle(graph):
    num_vertices = len(graph)

    # 0 -> UNSEEN
    # 1 -> SEEN
    # 2 -> PROCESSED
    state = {}
    for i in range(num_vertices):
        state[i] = 0 

    # for each v, store which vertex discovered it
    parent_discovered = {}

    # store vertices found as start/end of cycle
    cycles = set()

    for i in range(num_vertices):
        if state[i] == 0: # UNSEEN
            dfs(graph, i, state, parent_discovered, cycles)
    
    for v in cycles:
        seen = set()
        path = []
        while v not in seen:
            path.append(v)
            seen.add(v)
            v = parent_discovered[v]
        path.append(v)
        print(path)

         
    

    


# cycle: 3->4->5->3
graph = [
    [1, 2, 3], #0
    [2],       #1
    [],        #2
    [4],       #3
    [5],       #4
    [3]        #5
]

detectCycle(graph)