class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertIntoBST(root, val):
    if not root:
        root = TreeNode(val)
    elif val < root.val:
        if root.left:
            insertIntoBST(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            insertIntoBST(root.right, val)
        else:
            root.right = TreeNode(val)
            
    return root