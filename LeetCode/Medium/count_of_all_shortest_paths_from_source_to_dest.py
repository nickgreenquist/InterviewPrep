import heapq

class Solution:

    def countPaths(self, n, roads):
        if n <= 1:
            return 1
        
        # convert roads to AdjacenyList
        graph = {}
        for edge in roads:
            src = edge[0]
            dest = edge[1]
            w = edge[2]
            
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []
            
            graph[src].append((dest, w))
            graph[dest].append((src, w))
        
        heap = []
        heapq.heappush(heap, (0, 0))
        
        dist = {}
        for i in range(n):
            dist[i] = 1000000000000
        dist[0] = 0
        
        path = {} # where we came from
        count = {} # number of times getting to node with shortest cost
        for i in range(n):
            count[i] = 0
        count[0] = 1
        
        while heap:
            current_distance, min_v = heapq.heappop(heap)
            
            for edge in graph[min_v]:
                dest = edge[0]
                w = edge[1]

                potential_dist = current_distance + w
                if potential_dist == dist[dest]:
                    count[dest] += count[min_v]
                if potential_dist < dist[dest]:
                    dist[dest] = potential_dist
                    path[dest] = min_v # shortest path to dest came from min_v
                    count[dest] = count[min_v]
                    heapq.heappush(heap, (dist[dest], dest))
                 
        return count[n-1] % 1000000007
            
'''
Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
'''
s = Solution()
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

print(s.countPaths(n, roads))

