class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def flatten(root):
    if root:
        if root.left is None and root.right is None:
            return root, root
        
        lh, lt = flatten(root.left)
        rh, rt = flatten(root.right)
        root.left = None
        
        if lt is None:
            root.right = rh
            return root, rt
        if rh is None:
            root.right = lh
            return root, lt
        
        root.right = lh
        lt.right = rh
        return root, rt
    
    return None, None

def print_ll(head):
    s = ""
    while head:
        s += str(head.val) + "->"
        head = head.right
    print(s)

head = Node(1)
head.left = Node(2)
head.right = Node(3)
head.right.left = Node(4)

head, tail = flatten(head)
print_ll(head)