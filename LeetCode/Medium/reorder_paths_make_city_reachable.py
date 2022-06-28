class Solution:
    def minReorder(self, n, connections):
        
        graph = [[] for i in range(n)]
        for c in connections:
            v = c[0]
            u = c[1]
            graph[v].append(u)
        
        can_reach = {}
        for i in range(n):
            can_reach[i] = False
        can_reach[0] = True
        
        rev = [[] for i in range(n)]
        for v in range(n):
            for u in graph[v]:
                rev[u].append(v)
        
        q = []
        q.append(0)
        count = 0
        while q:
            v = q.pop()
            
            # find all neighbors (v->neighbor, or neighbor->v)
            neighbors = []
            wrong_way = set()
            for u in graph[v]:
                wrong_way.add(u)
                neighbors.append(u)
            for u in rev[v]:
                neighbors.append(u)
                
            for u in neighbors:
                if can_reach[u]:
                    continue
                    
                # if path was v->u and not back
                if u in wrong_way:
                    count += 1
                    
                can_reach[u] = True   
                q.append(u)
        
        return count

'''
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
'''

s = Solution()
print(s.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))