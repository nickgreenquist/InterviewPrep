
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if len(inorder) > 0:
        # get the root index from inorder list using the first element in preorder list
        root_index = inorder.index(preorder.pop(0))
        
        root = TreeNode(inorder[root_index])

        # we know the left subtree and right subtrees are to the left and 
        # right of the root index in the inorder list
        root.left = buildTree(preorder, inorder[0:root_index])
        root.right = buildTree(preorder, inorder[root_index + 1:])
        return root

def inorderPrint(root):
    if root:
        inorderPrint(root.left)
        print(root.val)
        inorderPrint(root.right)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = buildTree(preorder, inorder)

# print the tree to ensure it worked
inorderPrint(root)
