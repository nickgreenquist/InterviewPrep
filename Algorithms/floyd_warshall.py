
INF  = 1000
def floydWarshall(graph):
    V = len(graph)
    #dist[][] lookup table
    dist = [[INF for x in range(V)] for y in range(V)] 

    #fill up edge costs using graph
    for i in range(0, V):
        for j in range(0, V):
            if graph[i][j] < INF:
                dist[i][j] = graph[i][j]
     
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j],dist[i][k]+ dist[k][j])
    return dist

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

dist = floydWarshall(graph)

# Print the solution using np pretty print
import numpy as np
dist = np.array(dist)
print(dist)