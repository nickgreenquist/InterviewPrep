'''
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.
'''
def dfs(graph, v, seen, path, paths):
    if v in seen:
        return
    seen.add(v)
    path.append(v)
    if v == len(graph) - 1:
        paths.append(path[:])
    else: 
        for neighbor in graph[v]:
            dfs(graph, neighbor, seen, path, paths)
    seen.remove(v)
    path.pop()
    
def allPathsSourceTarget(graph):
    seen = set()
    path = []
    paths = []
    dfs(graph, 0, seen, path, paths)
    return paths
'''
Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
'''
print(allPathsSourceTarget([[1,2], [3], [3], []]))