# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root):
    stack = []
    output = []
    while root or len(stack) > 0:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        output.append(root.val)
        root = root.right
    return output

'''
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
'''
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(inorderTraversal(root))

