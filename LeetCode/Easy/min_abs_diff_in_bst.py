# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build(root, arr = []):
    if root:
        build(root.left, arr)
        arr.append(root.val)
        build(root.right, arr)
        return arr

def getMinimumDifference(root):
    nums = build(root, [])
    md = float('inf')
    for i in range(len(nums) - 1):
        md = min(md, abs(nums[i] - nums[i+1]))
    return md

'''
   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
'''
root = TreeNode(1)
root.right = TreeNode(3)
root.right.right = TreeNode(2)
print(getMinimumDifference(root))