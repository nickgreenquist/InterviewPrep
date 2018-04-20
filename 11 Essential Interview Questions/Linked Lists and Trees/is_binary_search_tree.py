class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_binary_search_tree(head, min_allowed, max_allowed):
    if head is None:
        return True
    if head.val < min_allowed or head.val > max_allowed:
        return False
    right = is_binary_search_tree(head.right, head.val, max_allowed)
    left = is_binary_search_tree(head.left, min_allowed, head.val)
    return left and right

# Set up tree
head = Node(4)
head.left = Node(1)
head.left.left = Node(0)
head.left.right = Node(2)
head.right = Node(5)
head.right.left = Node(3)
head.right.right = Node(6)

print(is_binary_search_tree(head, float('-inf'), float('inf')))