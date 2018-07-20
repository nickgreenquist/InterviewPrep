class BiNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def convert_to_dll(node):
    if node is None:
        return node, node
    left1 = node
    right2 = node
    
    if node.left is not None:
        left1, right1 = convert_to_dll(node.left)
        right1.right = node
        node.left = right1

    if node.right is not None:
        left2, right2 = convert_to_dll(node.right)
        left2.left = node
        node.right = left2

    return left1, right2

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.value)
    in_order_traversal(node.right)

root = BiNode(4)
root.left = BiNode(2)
root.left.left = BiNode(1)
root.left.left.left = BiNode(0)
root.left.right = BiNode(2)
root.left.right = BiNode(3)
root.right = BiNode(5)
root.right.right = BiNode(6)

left, right = convert_to_dll(root)

# traverse the list and print, ensure it goes 0 -> 6
node = left
while node:
    print(node.value)
    node = node.right