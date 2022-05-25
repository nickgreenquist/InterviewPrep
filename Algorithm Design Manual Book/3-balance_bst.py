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

def max_depth(node):
    if node is None:
        return 0
    return 1 + max(max_depth(node.right), max_depth(node.left))

def bst_to_arr(node):
    if node is None:
        return []
    
    return bst_to_arr(node.left) + [node.val] + bst_to_arr(node.right)

def arr_to_bst(start, end, a):
    n = end - start
    if n < 0 or start < 0 or end >= len(a):
        return None
    if n == 0:
        return Node(a[start])

    m = start + (n // 2)
    mid = a[m]
    node = Node(mid)
    node.left = arr_to_bst(start, m-1, a)
    node.right = arr_to_bst(m+1, end, a)

    return node


# Create imbalanced BST
# 1
#  \
#   2
#    \
#     3
#      \
#       4
head = Node(1)
head.right = Node(2)
head.right.right = Node(3)
head.right.right.right = Node(4)

inorder(head)

depth = max_depth(head)
print("Depth: " + str(depth))
print()

# Balance the BST, print should be the same
a = bst_to_arr(head)
print(a)
print()

head2 = arr_to_bst(0, len(a) - 1, a)
inorder(head)

depth = max_depth(head2)
print("Depth: " + str(depth))
print()

