
INF  = 1000
def floydWarshall(graph):
    V = len(graph)
    #dist[][] lookup table
    dist = [[INF for x in range(V)] for y in range(V)] 

    # next[][] path table
    next = [[-1 for x in range(V)] for y in range(V)]

    #fill up edge costs using graph
    for i in range(0, V):
        for j in range(0, V):
            if graph[i][j] < INF:
                dist[i][j] = graph[i][j]
                next[i][j] = j
    
    # fill up edge costs from v to v
    for i in range(V):
        dist[i][i] = 0
        next[i][i] = i
    
    # k acts as a 'visit this right before j' node, so k is in between the path from i->j
    # for every k, check if i->k + k->j is better than the straight distance from i->j
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist_with_k = dist[i][k]+ dist[k][j]
                if dist_with_k < dist[i][j]:
                    dist[i][j] = dist_with_k
                    next[i][j] = next[i][k]
    return dist, next

def getPath(next, v, u):
    if next[v][u] == -1:
        return None
    path = [v]
    while v != u:
        v = next[v][u]
        path.append(v)
    return path

# Driver program to test the above program
# Let us create the following weighted graph
"""
            10
       (0)------->(3)\\
        |         /|\  \\
      5 |          |     \\  5
        |          | 1     \\
       \|/         |         \\
       (1)------->(2)-------->(4)
            3           10        
"""
graph = [
            [0,5,INF,10,INF],
            [INF,0,3,INF,INF],
            [INF, INF, 0,   1, 10],
            [INF, INF, INF, 0, 5],
            [INF, INF, INF, INF, 0]
        ]

dist, next = floydWarshall(graph)

# Print the solution using np pretty print
import numpy as np
dist = np.array(dist)
print(dist)

print()
print("distance from v to u", 0, 4, dist[0][4])
print("path from v to u", 0, 4, getPath(next, 0, 4))