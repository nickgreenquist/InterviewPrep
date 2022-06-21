class Solution:      
    def dfs(self, graph, v, seen, processed):
        seen.add(v)
        
        for u in graph[v]:
            if u in seen:
                self.has_cycle = True
                break
                
            if u not in processed:
                self.dfs(graph, u, seen, processed)
        
        seen.remove(v)
        processed.add(v)
        
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # make graph from pre-reqs
        graph = [[] for i in range(numCourses)]
        for p in prerequisites:
            src = p[0]
            target = p[1]
            graph[src].append(target)
        
        self.has_cycle = False
        processed = set()
        seen = set()
        for v in range(numCourses):
            if v not in seen and v not in processed:
                self.dfs(graph, v, seen, processed)
        
        return not self.has_cycle

s = Solution()
prerequisites = [[1,0],[0,1]]
print(s.canFinish(2, prerequisites))

prerequisites = [[1,0]]
print(s.canFinish(2, prerequisites))