class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def traverse(root, is_left):
    if root:
        if not root.left and not root.right and is_left:
            return root.val
        left = traverse(root.left, True)
        right = traverse(root.right, False)
        return left + right
    else:
        return 0
        
def sumOfLeftLeaves(root):
    return traverse(root, False)

'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sumOfLeftLeaves(root))