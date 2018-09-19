'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create(nums, l, r):
    if r >= l:
        mid = int(l + (r - l) / 2)
        root = TreeNode(nums[mid])
        root.left = create(nums, l, mid - 1)
        root.right = create(nums, mid + 1, r)
        return root
    
def sortedArrayToBST(nums):
    root = create(nums, 0, len(nums) - 1)
    return root

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val)
        inorderTraversal(root.right)

'''
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
arr = [-10,-3,0,5,9]
root = sortedArrayToBST(arr)
inorderTraversal(root)
