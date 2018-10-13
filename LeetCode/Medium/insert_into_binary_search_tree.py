def insertIntoBST(root, val):
    if not root:
        root = TreeNode(val)
    elif val < root.val:
        if root.left:
            self.insertIntoBST(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            self.insertIntoBST(root.right, val)
        else:
            root.right = TreeNode(val)
            
    return root