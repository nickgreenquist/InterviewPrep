# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bstToGst(self, root: TreeNode) -> TreeNode:
    
    self.curr_sum = 0
    def traverse(root):
        if root:
            traverse(root.right)
            tmp = root.val
            root.val += self.curr_sum
            self.curr_sum += tmp
            traverse(root.left)
        return 0
            

    traverse(root)
    return root

