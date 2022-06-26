class Solution:      
    def dfs(self, graph, v, state, parent):
        state[v] = 1
        
        for u in graph[v]:
            if state[u] == 1:
                parent[u] = v
                self.cycles.add(u)
                break 
            elif state[u] == 0:
                parent[u] = v
                self.dfs(graph, u, state, parent)
        
        state[v] = 2
        
    def findCycles(self, graph):
        self.cycles = set()

        state = {}
        for v in range(len(graph)):
            state[v] = 0
        
        parent = {}
        for v in range(len(graph)):
            if state[v] == 0:
                self.dfs(graph, v, state, parent)
        
        # construct all cycle paths
        cycles = []
        for v in self.cycles:
            seen = set()
            path = []
            current = v
            while current not in seen:
                path.append(current)
                seen.add(current)
                current = parent[current]
            cycles.append(path)
        
        for cycle in cycles:
            print(cycle)

# cycle: 3->4->5->3
# cycle: 0->1->0
graph = [
    [1, 2, 3], #0
    [0, 2],       #1
    [],        #2
    [4],       #3
    [5],       #4
    [3]        #5
]
s = Solution()
s.findCycles(graph)