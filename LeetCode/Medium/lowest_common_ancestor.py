# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LCA_Solution(object):
    def lca(self, root, p, q, already_found_p, already_found_q):
        if root:
            found_p = False
            found_q = False
            if root.val == p.val:
                found_p = True
            if root.val == q.val:
                found_q = True
            
            if (already_found_p or found_p) and (already_found_q and found_q):
                return True, True
            
            for child in [root.left, root.right]:
                c_found_p, c_found_q = self.lca(child, p, q, found_p, found_q)
                found_p = found_p or c_found_p
                found_q = found_q or c_found_q
                if found_p and found_q:
                    self.ancestor = root
                    return False, False
            return (found_p or already_found_p), (found_q or already_found_q)
        else:
            return False, False
    def lowestCommonAncestor(self, root, p, q):
        self.ancestor = root
        self.lca(root, p, q, False, False)
        return self.ancestor

'''
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
'''
root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
print(LCA_Solution().lowestCommonAncestor(root, root.left, root.left.right.right).val)