class UnionFind:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.size = [1 for i in range(num_vertices)]
        self.parent = [i for i in range(num_vertices)]
        self.numComponents = num_vertices

    def find(self, v):
        root = v
        while root != self.parent[root]:
            root = self.parent[root]
        
        # compress paths
        while v != root:
            next = self.parent[v]
            self.parent[v] = root
            v = next
        return root

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        
        # merge smaller path into larger path
        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        
        self.numComponents -= 1
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Graph(object):
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.edges = [] # list of single tuple edges

    def addEdge(self, u, v, w):
        # store triple containing the edge + weight
        self.edges.append([u,v,w])

def kruskal_mst(G):

    # Step 1: sort all edges in non-decreasing order of weights
    edges = sorted(G.edges, key=lambda x: x[2])

    uf = UnionFind(G.V)
    mst_edges = []

    # Step 2: Loop over all sorted edges and union x and y if not connected.
    for edge in edges:
        x = edge[0]
        y = edge[1]
        w = edge[2]

        rootX = uf.find(x)
        rootY = uf.find(y)

        if rootX == rootY:
            continue
        
        uf.union(x, y)
        mst_edges.append([x, y, w])

    return mst_edges

# Driver code to test MST
g = Graph(6) 

g.addEdge(0, 1, 7) 
g.addEdge(0, 2, 8) 

g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 6) 
g.addEdge(1, 5, 15)

g.addEdge(2, 3, 4) 
g.addEdge(2, 5, 3) 

g.addEdge(3, 4, 5) 
g.addEdge(3, 5, 2) 

g.addEdge(4, 5, 2)

mst_edges = kruskal_mst(g)
print(sorted(mst_edges, key=lambda x: x[0]))

'''
Time Complexity: O(ElogE) or O(ElogV).
Sorting of edges takes O(ELogE) time.
After sorting, we iterate through all edges and apply find-union algorithm.
The find and union operations take amortized O(1) time. 
So overall complexity is O(ELogE + ELogV) time.

The value of E can be atmost O(V2), so O(LogV) and O(LogE) are the same.
Therefore, overall time complexity is O(ElogE) or O(ElogV)
'''