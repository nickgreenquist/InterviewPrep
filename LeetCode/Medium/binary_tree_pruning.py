# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pruneTree(self, root: TreeNode) -> TreeNode:
    
    def traverse(root):
        if root:
            root.left = traverse(root.left)
            root.right = traverse(root.right)
            if root.left or root.right or root.val == 1:
                return root
            else:
                return None
        return None
    
    return traverse(root)

