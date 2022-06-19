class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #define NO_CAMERA       0
    #define HAS_CAMERA      2
    #define COVERED         1
    
    def setupVCHashDriver(self):
        self.answer = 0
        
    def vertexCover(self, node):
        if not node:
            return 1 # COVERED
        
        left = self.vertexCover(node.left)
        right = self.vertexCover(node.right)
        if (left == 0 or right == 0): # EITHER HAS NO_CAMERA
            self.answer += 1
            return 2 # HAS_CAMERA
        elif (left == 2 or right == 2): # EITHER HAS_CAMERA
            return 1 # COVERED
        else:
            return 0 # NO_CAMERA
        
        
            
    def minCameraCover(self, root) -> int:
        if not root:
            return 0
        if root and not root.left and not root.right:
            return 1
        
        # first, set up global ans, then run
        self.setupVCHashDriver()
        
        # run from root, and final check for if we need camera at root.
        res = self.vertexCover(root)
        if res == 0: # NO_CAMERA
            self.answer += 1
            
        return self.answer
    
# one camera at root.left covers all 4 nodes in tree
root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)

s = Solution()
print(s.minCameraCover(root))