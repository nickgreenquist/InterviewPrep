'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
and node values with a subtree of s. A subtree of s is a tree consists of a node in s
and all of this node's descendants. The tree s could also be considered as a subtree of itself.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isEqual(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    if s.val != t.val:
        return False
    return isEqual(s.left, t.left) and isEqual(s.right, t.right)

def look(s, t):
    if s and t:
        if s.val == t.val:
            if isEqual(s, t):
                return True
        return look(s.left, t) or look(s.right, t)
    return False
    
def isSubtree(s, t):
    return look(s,t)

'''
Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
'''
s = TreeNode(3)
s.left = TreeNode(4)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)
s.right = TreeNode(5)

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)

print(isSubtree(s,t))


'''
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''
s.left.right.left = TreeNode(0)
print(isSubtree(s,t))
        