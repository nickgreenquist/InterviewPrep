class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isValid(root, left, right):
    if root is None:
        return True
    
    # Check if in bounds set by parents
    if root.val <= left or root.val >= right:
        return False
    
    left_valid = False
    if root.left is None:
        left_valid = True
        
    right_valid = False
    if root.right is None:
        right_valid = True
        
    if root.left:
        left_valid = isValid(root.left, left, root.val) and root.val > root.left.val
    if root.right:
        right_valid = isValid(root.right, root.val, right) and root.val < root.right.val
    return left_valid and right_valid
    
    
def isValidBST(root) -> bool:
    if root is None:
        return True
    
    return isValid(root, float('-inf'), float('inf'))


head = Node(3)
head.left = Node(1)
head.left.right = Node(2)
head.right = Node(4)

# expect True
print(isValidBST(head))

head = Node(5)
head.left = Node(1)
head.right = Node(4)
head.right.left = Node(3) # 3 < 5; error
head.right.right = Node(6)

# expect False
print(isValidBST(head))