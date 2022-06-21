class Solution:
    def dfs(self, graph, cur, path):
        path.append(cur)
        for v in graph[cur]:      
            if v == len(graph) - 1:
                self.paths.append(path.copy() + [v])
            else:
                self.dfs(graph, v, path)
        path.pop()
        
    def allPathsSourceTarget(self, graph):
        self.paths = []
        self.dfs(graph, 0, path=[])
        return self.paths

s = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(s.allPathsSourceTarget(graph))