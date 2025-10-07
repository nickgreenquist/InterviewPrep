from typing import List

def countComponents(n: int, edges: List[List[int]]) -> int:
    graph = {}
    for edge in edges:
        src = edge[0]
        dest = edge[1]
        if src not in graph:
            graph[src] = []
        if dest not in graph:
            graph[dest] = []
        graph[src].append(dest)
        graph[dest].append(src)
    
    visited = {}
    for node in graph.keys():
        visited[node] = False
    
    def dfs(node):
        for dest in graph[node]:
            if not visited[dest]:
                visited[dest] = True
                dfs(dest)

    num_components = 0
    for node in graph.keys():
        if not visited[node]:
            visited[node] = True
            dfs(node)
            num_components += 1
    return num_components

'''
Input:
n=3
edges=[[0,1], [0,2]]
Output: 1


Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]
Output: 2
'''

print(countComponents(n=3, edges=[[0,1], [0,2]]))
print(countComponents(n=6, edges=[[0,1], [1,2], [2,3], [4,5]]))

