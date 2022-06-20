class Solution:
    def getOppositeColor(self, color):
        if color == 'RED':
            return 'BLUE'
        elif color == 'BLUE':
            return 'RED'
        return None
    
    def isBipartite(self, graph) -> bool:
        num_vertices = len(graph)
        if num_vertices < 1:
            return True
        
        # set up coloring map
        color_arr = [-1] * num_vertices
        
        # loop over every vertice, and perform 2-coloring on each connected component
        seen = set()
        for i in range(num_vertices):
            if i in seen:
                continue
                
            q = []
            q.append(i)
            color_arr[i] = 'RED'
            seen.add(i)

            while q:
                v = q.pop()

                for u in graph[v]:
                    if v == u:
                        return False

                    # uncolored - color with opposite, add to Queue, and add to seen
                    if color_arr[u] == -1:
                        color_arr[u] = self.getOppositeColor(color_arr[v])
                        q.append(u)
                        seen.add(u)
                    elif color_arr[u] == color_arr[v]:
                        return False
        
        return True

s = Solution()
graph = [[1,3],[0,2],[1,3],[0,2]]
print(s.isBipartite(graph))