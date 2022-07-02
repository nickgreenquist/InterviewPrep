INF = 100000
class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        dist = [[INF for i in range(n)] for j in range(n)]
        for edge in edges:
            v = edge[0]
            u = edge[1]
            w = edge[2]
            dist[v][u] = w
            dist[u][v] = w
            
        for i in range(n):
            dist[i][i] = 0
        
        # for every k, check if i->k + k->j is better than the straight distance from i->j
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist_with_k = dist[i][k] + dist[k][j]
                    dist[i][j] = min(dist[i][j], dist_with_k)
                        
        reachable = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if dist[i][j] > 0 and dist[i][j] <= distanceThreshold:
                    reachable[i] += 1
        
        min_reachable_cities = n
        city_with_min_reachable_cities = -1
        for i in range(n):
            if reachable[i] <= min_reachable_cities:
                min_reachable_cities = reachable[i]
                city_with_min_reachable_cities = i
        return city_with_min_reachable_cities

'''
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
'''

s = Solution()

n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2
print(s.findTheCity(n, edges, distanceThreshold))
