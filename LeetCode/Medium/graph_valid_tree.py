'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.
'''

from typing import List

def validTree(n: int, edges: List[List[int]]) -> bool:
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
    
    def dfs(parent, node):
        for dest in graph[node]:
            if dest == parent: # don't go back to parent
                continue
            if visited[dest]: # cycle
                return True
            
            visited[dest] = True
            has_cycle = dfs(node, dest)
            if has_cycle:
                return True
        return False
    
    for node in graph.keys():
        if not visited[node]:
            visited[node] = True
            has_cycle = dfs(-1, node)
            if has_cycle:
                return False
    
    # if we visited all nodes and never found cycle above
    return all(visited.values())

'''
Input:
n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true

Input:
n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false
'''

print(validTree(n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(validTree(n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))