# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root):
        if root is None:
            return 0
        
        left = self.check(root.left)
        right = self.check(root.right)
        
        if left - right > 1 or right - left > 1:
            self.isBalanced = False
        
        return max(left, right) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        self.isBalanced = True
        
        left = self.check(root.left)
        right = self.check(root.right)
      
        if left - right > 1 or right - left > 1:
            self.isBalanced = False
        
        return self.isBalanced