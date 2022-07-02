import heapq

class Solution:
    def dijkstras(self, graph, k, n):
        dist = [10000 for i in range(n)]
        dist[k] = 0
        processed = set()
        
        heap = []
        heapq.heappush(heap, (0, k))
        
        while heap:
            current_dist, v = heapq.heappop(heap)
            processed.add(v)
            for edge in graph[v]:
                u = edge[0]
                w = edge[1]
                if current_dist + w < dist[u] and u not in processed:
                    dist[u] = current_dist + w
                    heapq.heappush(heap, (dist[u], u))
        return dist, processed
            
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for i in range(n)]
        for edge in times:
            v = edge[0]
            u = edge[1]
            w = edge[2]
            graph[v-1].append([u-1, w])
        
        dist, processed = self.dijkstras(graph, k-1, n)
        
        if len(processed) < n:
            return -1
        return max(dist)