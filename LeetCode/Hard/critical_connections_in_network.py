class Solution:      
    def dfs(self, graph, v, k, rank):
        if rank[v] >= 0: # SEEN or PROCESSED
            return rank[v]
        
        rank[v] = k
        min_rank = k

        for u in graph[v]:
            if rank[u] == k - 1: # PARENT
                continue
                
            # DFS into u, and return earliest ancestor reachable from u
            min_rank_u = self.dfs(graph, u, k + 1, rank)
            
            # found ancestor, so cut connection from v to u
            if min_rank_u <= k:
                self.cycle_edges.add((v,u))
                self.cycle_edges.add((u,v))
                
            # update earliest ancestor we found
            min_rank = min(min_rank, min_rank_u)
        
        rank[v] = len(graph)
        return min_rank
        
        
    def findCycles(self, graph):
        self.cycle_edges = set()

        rank = {}
        for v in range(len(graph)):
            rank[v] = -2
        
        for v in range(len(graph)):
            self.dfs(graph, v, 0, rank)
        
        return self.cycle_edges
            
    def criticalConnections(self, n, connections):
        connections_clean = [[] for i in range(n)]
        for edge in connections:
            v = edge[0]
            u = edge[1]
            connections_clean[v].append(u)
            connections_clean[u].append(v)
                
        # find all cycle edges in the graph to remove
        cycle_edges = self.findCycles(connections_clean)
        
        # remove all edges from graph where v and u are in same path
        graph = [[] for i in range(n)]
        for v in range(n):
            for u in connections_clean[v]:
                if (v,u) not in cycle_edges:
                    graph[v].append(u)
        
        critical_components = []
        critical_components_seen_util = set()
        for v in range(n):
            for u in graph[v]:
                edge1 = str(v) + ':' + str(u)
                edge2 = str(u) + ':' + str(v)
                if edge1 not in critical_components_seen_util and edge2 not in critical_components_seen_util:
                    critical_components.append([v,u])
                    critical_components_seen_util.add(edge1)
                    critical_components_seen_util.add(edge2)
        return critical_components

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

s = Solution()
print(s.criticalConnections(n, connections))