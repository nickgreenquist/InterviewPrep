# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def look(root, p, q):
            if root is None:
                return None
            
            found_here = False
            if root.val == p:
                found_here = True
            if root.val == q:
                found_here = True
            
            
            left, right = None, None
            if p < root.val:
                left = look(root.left, p, q)
            if q > root.val:
                right = look(root.right, p, q)
            
            if (found_here and left) or (found_here and right) or (left and right):
                self.ans = root
            if found_here or left or right:
                return root

            return None
        
        look(root, min(p.val, q.val), max(p.val, q.val))
        return self.ans