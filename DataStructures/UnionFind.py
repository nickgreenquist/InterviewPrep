class UnionFind:
    def __init__(self, nums):
        n = len(nums)
        self.n = n
        self.size = [1 for i in range(n)]
        self.parent = [i for i in range(n)]
        self.numComponents = n

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
