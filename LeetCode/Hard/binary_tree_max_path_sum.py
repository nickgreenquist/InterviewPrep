'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node
to any node in the tree along the parent-child connections. 

The path must contain at least one node and does not need to go through the root.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BestPathFinder(object):
    def __init__(self, root):
        self.root = root
        self.best = float('-inf')
        
    def traverse(self, root):
        if root:
            left = self.traverse(root.left)
            right = self.traverse(root.right)
            
            # store possible best seen yet
            self.best = max(self.best, left + root.val + right, left + root.val, right + root.val, root.val)
            
            # return best path that includes this node
            return max(left + root.val, root.val, root.val + right)    
        else:
            return float('-inf')
        
    def find(self):
        self.traverse(self.root)
        return self.best

'''
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(BestPathFinder(root).find())