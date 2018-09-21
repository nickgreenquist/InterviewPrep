# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.max_d = 0
        
    def diameterOfBinaryTreeHelper(self, root):
        if root:
            max_l = self.diameterOfBinaryTreeHelper(root.left)
            max_r = self.diameterOfBinaryTreeHelper(root.right) 
            self.max_d = max(self.max_d, max_l + max_r)
            return max(max_l, max_r) + 1
        return 0
    
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.diameterOfBinaryTreeHelper(root)
        return self.max_d
'''
Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
print(Solution().diameterOfBinaryTree(root))