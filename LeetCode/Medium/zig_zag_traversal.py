class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    if not root:
        return []
    q = [root]
    left = True
    out = []
    while q:
        row = []
        toadd = []
        while q:
            e = q.pop(0)
            row.append(e.val)
            toadd.append(e)

        # add all children back to q
        for e in toadd:
            if e.left:
                q.append(e.left)
            if e.right:
                q.append(e.right)
                
        if not left:
            row = row[::-1]
        out.append(row)
        left = not left
    return out
'''
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(zigzagLevelOrder(root))
