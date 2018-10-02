# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    
    root = TreeNode(postorder.pop())
    index = inorder.index(root.val)
    
    root.right = buildTree(inorder[index+1:], postorder)
    root.left = buildTree(inorder[:index], postorder)
    return root

def inorderPrint(root):
    if root:
        inorderPrint(root.left)
        print(root.val)
        inorderPrint(root.right)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root = buildTree(inorder, postorder)

# print the tree to ensure it worked
inorderPrint(root)