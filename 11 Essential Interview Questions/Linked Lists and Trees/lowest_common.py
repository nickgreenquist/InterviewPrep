class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def path_to_x(head, x):
    if head is None:
        return None
    if head.val == x:
        return str(x)
    path = str(head.val)
    left = path_to_x(head.left, x)
    if left:
        return path + left
    right = path_to_x(head.right, x)
    if right:
        return path + right
    return None

def lca(head, v1, v2):
    path_to_v1 = path_to_x(head, v1)
    path_to_v2 = path_to_x(head, v2)
    if path_to_v1 is None or path_to_v2 is None:
        return None

    common_ancestor = str(head.val)
    i = 0
    while i < len(path_to_v1) and i < len(path_to_v2):
        if path_to_v1[i] == path_to_v2[i]:
            common_ancestor = path_to_v1[i]
            i += 1
        else:
            break
    return common_ancestor

# Set up tree
head = Node(5)
head.left = Node(1)
head.left.left = Node(3)
head.left.right = Node(8)
head.left.left.left = Node(6)
head.left.left.right = Node(7)
head.right = Node(4)
head.right.left = Node(9)
head.right.right = Node(2)

print(lca(head, 7,1))