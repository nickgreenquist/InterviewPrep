class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recoverFromPreorder(S):
    stack = []
    i = 0
    while i < len(S):
        depth = 0
        val = ""
        while i < len(S) and S[i] == '-':
            depth += 1
            i += 1
        while i < len(S) and S[i] != '-':
            val = val + S[i]
            i += 1
        node = TreeNode(val)
        
        # 'climb' back up the stack, which holds the root node above us
        while depth < len(stack):
            stack.pop()
            
        # check if left or right child
        if stack:
            root = stack[-1]
            if root.left is None:
                root.left = node
            else:
                root.right = node
        stack.append(node)
    return stack[0]

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

'''
Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
'''
root = recoverFromPreorder("1-2--3--4-5--6--7")
inorder(root)