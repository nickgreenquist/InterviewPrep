class Vertex():
    def __init__(self, val):
        self.val = val
        self.edges = set()

# Unweighted, directed Graph
class Graph():
    def __init__(self):
        self.vertices = {}
    
    def insert(self, val):
        if val not in self.vertices:
            self.vertices[val] = Vertex(val)
    
    def insert_edge(self, source, dest):
        if source not in self.vertices:
            self.vertices[source] = Vertex(source)
        if dest not in self.vertices:
            self.vertices[dest] = Vertex(dest)

        self.vertices[source].edges.add(self.vertices[dest])
    
    def insert_edges(self, source, destinations):
        for dest in destinations:
            self.insert_edge(source, dest)

    def dfs(self, node, seen):
        seen.add(node.val)
        processed = []
        
        for v in node.edges:
            if v.val not in seen:
                processed += self.dfs(v, seen)

        # finished processing node
        processed.append(node.val)
        return processed
    
    def top_sort(self):
        seen = set()
        processed = []

        for v_val in self.vertices.keys():
            if v_val not in seen:
                processed += self.dfs(self.vertices[v_val], seen)
        return processed

G = Graph()
G.insert_edges('A', ['B', 'C'])
G.insert_edges('B', ['C', 'D', 'E'])
G.insert_edges('C', ['F'])
G.insert_edges('D', ['E', 'G'])
G.insert_edges('E', ['F', 'G'])
G.insert_edges('F', [])
G.insert_edges('G', ['F', 'I'])
G.insert_edges('H', ['F', 'G', 'J'])
G.insert_edges('I', ['J'])
G.insert_edges('J', [])

top_sort = G.top_sort()

# reversed order of fully processed nodes is a top-sort of G.
print(top_sort[::-1])