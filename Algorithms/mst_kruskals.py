from collections import defaultdict

class Graph(object):
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.G = [] #adjacency list

    def addEdge(self, u, v, w):
        # store triple containing the edge
        self.G.append([u,v,w])

    # find the set of an element i
    def find_parent(self, parent, i):
        # check if you are your current parent
        if parent[i] == i:
            return i
        else:
            return self.find_parent(parent, parent[i])

    # union of x's set and y's set using the rank
    def union(self, parent, rank, x, y):
        parent_x = self.find_parent(parent, x)
        parent_y = self.find_parent(parent, y)

        # append the smaller rank tree under the root of the higher rank tree
        if rank[parent_x] < rank[parent_y]:
            parent[parent_x] = parent_y
        elif rank[parent_x] > rank[parent_y]:
            parent[parent_y] = parent_x
        else:
            # either can be parent, just increaes it's rank
            parent[parent_y] = parent_x
            rank[parent_x] += 1

    def kruskal(self):
        mst = []

        # Step 1: sort all edges in non-decreasing order of weights
        self.G = sorted(self.G, key=lambda x: x[2])

        parent = []
        rank = []

        for v in range(self.V):
            parent.append(v)
            rank.append(0)

        i = 0
        e = 0
        while e < self.V - 1:
            # Step 2: pick the smallest edge
            u,v,w = self.G[i]
            i += 1

            parent_u = self.find_parent(parent, u)
            parent_v = self.find_parent(parent, v)

            # check if this edge causes a cycle
            if parent_u != parent_v:
                e += 1 # select this edge
                mst.append([u,v,w])
                self.union(parent, rank, parent_u, parent_v)

        return mst

# Driver code to test MST
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
  
mst = g.kruskal() 
print(mst)

'''
Time Complexity: O(ElogE) or O(ElogV).
Sorting of edges takes O(ELogE) time.
After sorting, we iterate through all edges and apply find-union algorithm.
The find and union operations can take atmost O(LogV) time.
So overall complexity is O(ELogE + ELogV) time.

The value of E can be atmost O(V2), so O(LogV) and O(LogE) are the same.
Therefore, overall time complexity is O(ElogE) or O(ElogV)
'''