from collections import defaultdict

class Graph(object):
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.G = defaultdict(list) # ordered dict

    def add_edge(self, u, v):
        self.G[u].append(v)
        self.V += 1
    
    # find the set of an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        else:
            return self.find_parent(parent, parent[i])
    
    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    def detect_cycle(self):
        # creates slot for each vertex, initially -1 meaning single element subset
        parent = [-1]*(self.V)

        for i in self.G:
            for j in self.G[i]:
                parent_i = self.find_parent(parent, i)
                parent_j = self.find_parent(parent, j)
                if parent_i == parent_j:
                    return True
                self.union(parent, parent_i, parent_j)

G = Graph(3)
G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(2,0)

print("Has cycle: {}".format(G.detect_cycle()))