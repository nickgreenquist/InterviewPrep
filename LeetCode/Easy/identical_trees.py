class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p, q):
    if p and q:
        if p.val != q.val:
            return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    if p and not q:
        return False
    if q and not p:
        return False
    return True

'''
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
'''
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(isSameTree(root1, root2))