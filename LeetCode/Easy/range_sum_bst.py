# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def rangeSumBST(self, root, low, high):
    """
    :type root: Optional[TreeNode]
    :type low: int
    :type high: int
    :rtype: int
    """
    def traverse(root):
        if root is None:
            return 0
        left = traverse(root.left)
        right = traverse(root.right)
        val = root.val if root.val <= high and root.val >= low else 0
        return left + val + right
    return traverse(root)
    
