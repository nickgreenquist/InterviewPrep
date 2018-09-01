# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_symmetric(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    return is_symmetric(left.right, right.left) and is_symmetric(left.left, right.right)

def is_symmetric_driver(root):
    if not root:
        return True
    return is_symmetric(root.left, root.right)

"""
    1
   / \
  2   2
 / \ / \
3  4 4  3
"""
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(is_symmetric_driver(root))
