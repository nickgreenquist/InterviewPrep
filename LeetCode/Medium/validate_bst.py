# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValid(root, left, right):
    if root:
        if root.val <= left or root.val >= right:
            return False
        valid_left = not root.left
        valid_right = not root.right
        if not valid_left:
            valid_left = isValid(root.left, left, root.val) and root.val > root.left.val
        if not valid_right:
            valid_right = isValid(root.right, root.val, right) and root.val < root.right.val
        return valid_left and valid_right
    return True

def isValidBST(root):
    return isValid(root, float('-inf'), float('inf'))

'''
    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(isValidBST(root))