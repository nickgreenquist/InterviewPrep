from collections import deque
import copy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root):
    if not root:
        return []
    traversal = [[root.val]]
    q = deque([root])
    while len(q) > 0:
        row = []
        row_q = copy.copy(q)
        q = deque([])
            
        while len(row_q) > 0:
            root = row_q.popleft()
            if root.left:
                q.append(root.left)
                row.append(root.left.val)
            if root.right:
                q.append(root.right)
                row.append(root.right.val)
        if len(row) > 0:
            traversal.append(row)
            
    return traversal

'''
    3
   / \
  9  20
    /  \
   15   7

[
  [3],
  [9,20],
  [15,7]
]
'''
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrder(root))