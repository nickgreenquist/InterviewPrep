class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.seen = False

def DFS(node, goal):
    if not node:
        return False
    for n in node.neighbors:
        if n == goal:
            return True
        if not n.seen:
            n.seen = True
            if DFS(n, goal):
                return True
    return False

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.neighbors = [b,c]
c.neighbors = [d]
d.neighbors = [c]
print( DFS(c, b) )