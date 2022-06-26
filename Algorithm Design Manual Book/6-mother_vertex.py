def dfs(graph, v, state, processed):
    state[v] = 1 # SEEN

    for u in graph[v]:
        if state[u] == 2: # PROCESSED
            continue
        elif state[u] == 1: # SEEN
            print('CYCLE')
            continue
        else:
            dfs(graph, u, state, processed)
    
    state[v] = 2 # PROCESSED
    processed.append(v)

def findMother(graph):
    state = {}
    for i in range(len(graph)):
        state[i] = 0 # UNSEEN
    
    processed = []
    for v in range(len(graph)):
        if state[v] == 0: # UNSEEN
            dfs(graph, v, state, processed)
    
    potential_mother = processed[-1]
    processed_from_mother = []
    state = {}
    for i in range(len(graph)):
        state[i] = 0 # UNSEEN

    dfs(graph, potential_mother, state, processed_from_mother)

    # if we processed every vertex starting from mother, return true
    if len(processed_from_mother) == len(graph):
        return potential_mother
    return -1

graph = [
    [1,2],
    [3],
    [],
    [],
    [1],
    [2,6],
    [0,4]
]
print("A mother vertex is " + str(findMother(graph)))