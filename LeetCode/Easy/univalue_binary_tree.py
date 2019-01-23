'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def dfs(root, val):
    if not root:
        return True
    if root.val != val:
        return False
        
    return dfs(root.left, val) and dfs(root.right, val)

def isUnivalTree(root):
    if root:
        return dfs(root, root.val)
    return True

# Output: true
root1 = TreeNode(1)
root1.left = TreeNode(1)
root1.right = TreeNode(1)
print(isUnivalTree(root1))

# Output: false
root2 = TreeNode(2)
root2.left = TreeNode(2)
root2.right = TreeNode(5)
print(isUnivalTree(root2))