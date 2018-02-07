class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def BuildTree(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    node = Node(array[mid])
    node.left = BuildTree(array, start, mid - 1)
    node.right = BuildTree(array, mid + 1, end)
    return node

def InOrderPrint(node):
    if not node:
        return
    InOrderPrint(node.left)
    print(node.value)
    InOrderPrint(node.right)

def PreOrderPrint(node):
    if not node:
        return
    print(node.value)
    PreOrderPrint(node.left)
    PreOrderPrint(node.right)

array = [1,2,3,4,5,6,7,8,9,10]
root = BuildTree(array, 0, len(array) - 1)

print("In Order Traversal: ")
InOrderPrint(root)

print("\n\nPre Order Traversal: ")
PreOrderPrint(root)



