# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    valToNode = {}

    def Traverse(self, node):
        # make copy of this node
        newNode = Node()
        newNode.val = node.val
        newNode.neighbors = []
        self.valToNode[node.val] = newNode

        for neighbor in node.neighbors:
            if neighbor.val in self.valToNode:
                newNode.neighbors.append(self.valToNode[neighbor.val])
            else:
                newNode.neighbors.append(self.Traverse(neighbor))
        return newNode


    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.valToNode = {}

        if node is None:
            return node
        
        newNode = self.Traverse(node)
        return newNode