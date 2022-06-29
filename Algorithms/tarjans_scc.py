class Tarjan:
    def __init__(self, num_vertices, graph):
        self.V = num_vertices
        self.G = graph

    def dfs(self, v, ids, rank, stack, onStack, state):
        stack.append(v)
        onStack[v] = True
        state[v] = 1 # SEEN
        ids[v] = self.id + 1
        rank[v] = self.id + 1
        self.id += 1

        for u in self.G[v]:
            if state[u] == 0: # UNSEEN
                self.dfs(u, ids, rank, stack, onStack, state)
            if onStack[u]:
                rank[v] = min(rank[v], rank[u])
        
        # Check for SCC
        if ids[v] == rank[v]:
            # pop off all items from stack until we reach v
            while True:
                node = stack.pop()
                onStack[node] = False
                rank[node] = rank[v]
                if node == v:
                    break

    
    def scc(self):
        self.id = 0 # used to assign id to newly seen nodes
        state = {}
        
        ids = [0 for i in range(self.V)]
        rank = [0 for i in range(self.V)]
        onStack = [False for i in range(self.V)]
        stack = []

        for i in range(self.V):
            state[i] = 0 # UNSEEN
        for i in range(self.V):
            if state[i] == 0: # UNSEEN
                self.dfs(i, ids, rank, stack, onStack, state)
        
        # Map each SCC group to vertices in it
        scc_group_to_vertices = {}
        for i in range(len(rank)):
            scc_group = rank[i]
            if scc_group not in scc_group_to_vertices:
                scc_group_to_vertices[scc_group] = []
            scc_group_to_vertices[rank[i]].append(i)
        return scc_group_to_vertices
        

# Expected SCCs:
# {1: [0, 4], 2: [1, 2, 5], 5: [3, 6, 7]}
graph = [
    [1,4],
    [5],
    [1,3,6],
    [6],
    [0,5],
    [2,6],
    [7],
    [3]
]
solver = Tarjan(len(graph), graph)
scc_group_to_vertices = solver.scc()
print(scc_group_to_vertices)