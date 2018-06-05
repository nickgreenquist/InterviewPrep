class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

def invert(root):
    if root:
        invert(root.right)
        invert(root.left)
        temp = root.right
        root.right = root.left
        root.left = temp

root = TreeNode(4)
root.right = TreeNode(7)
root.right.right = TreeNode(9)
root.right.left = TreeNode(6)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.left = TreeNode(1)


'''
     4
   /   \
  2     7
 / \   / \
1   3 6   9
'''
inorder_traversal(root)

'''
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
print("inverted:")
invert(root)
inorder_traversal(root)