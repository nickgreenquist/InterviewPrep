# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traverse(self, root):
        if root:
            self.traverse(root.left)
            self.k -= 1
            
            if self.k == 0:
                self.answer = root.val
                return
            
            self.traverse(root.right)
        
    def kthSmallest(self, root, k):
        self.k = k
        self.answer = root.val
        self.traverse(root)
        return self.answer
    
'''
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
'''
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(6)

solver = Solution()
print(solver.kthSmallest(root, 3))