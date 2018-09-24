'''
Given a Binary Search Tree (BST) with the root node root,
return the minimum difference between the values of any two different nodes in the tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MinDiffSolver(object):
    def __init__(self):
        self.md = float('inf')
    
    def minDiffInBST(self, root):
        self.minDiffInBSTHelper(root)
        return self.md

    def minDiffInBSTHelper(self, root):
        # compare root.val to leftmost and rightmost values
        if root:
            left_l, right_l = self.minDiffInBSTHelper(root.left)
            left_r, right_r = self.minDiffInBSTHelper(root.right)
            if left_l:
                self.md = min(self.md, abs(root.val - left_l))
            if left_r:
                self.md = min(self.md, abs(root.val - left_r))
            if right_l:
                self.md = min(self.md, abs(root.val - right_l))
            if right_r:
                self.md = min(self.md, abs(root.val - right_r))
            
            if left_l and right_r:
                return left_l, right_r
            if left_l:
                return left_l, root.val
            if right_r:
                return root.val, right_r
            else:
                return root.val, root.val    
        else:
            return None, None

'''
Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
'''
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
print(MinDiffSolver().minDiffInBST(root))