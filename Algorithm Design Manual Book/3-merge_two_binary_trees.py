class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

def mergeTrees(root1, root2) -> Node:
    if not root1 and not root2:
        return None
    
    if root1 and not root2:
        return root1
    
    if root2 and not root1:
        return root2
    
    if root1 and root2:
        root1.val += root2.val

        root1.left = mergeTrees(root1.left, root2.left)
        root1.right = mergeTrees(root1.right, root2.right)

        return root1

head1 = Node(5)
head1.left = Node(2)
head1.left.left = Node(1)
head1.left.right = Node(3)
head1.right = Node(8)
head1.right.left = Node(6)

head2 = Node(5)
head2.left = Node(1)

head3 = mergeTrees(head1, head2)

inorder(head3)
