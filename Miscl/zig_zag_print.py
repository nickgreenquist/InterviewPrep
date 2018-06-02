import queue
import copy

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def zig_zag_print(root):
    q1 = queue.Queue()
    q2 = queue.Queue()
    q1.put(root)

    total_string = ''
    level_values = []
    level = 1
    while not q1.empty() or not q2.empty():
        while not q1.empty():
            node = q1.get()
            level_values.append(node.value)
            if node.left:
                q2.put(node.left)
            if node.right:
                q2.put(node.right)

        # copy queue
        while not q2.empty():
            q1.put(q2.get())

        if level % 2 == 0:
            level_values = level_values[::-1]
        total_string += str(level_values)
        level += 1
        level_values = []
    print(total_string)

root =  TreeNode(1)
root.left =  TreeNode(2)
root.right =  TreeNode(3)
root.left.left =  TreeNode(4)
root.left.right =  TreeNode(5)
root.right.left =  TreeNode(6)
root.right.right =  TreeNode(7)
root.left.right.left =  TreeNode(8)
root.left.right.right =  TreeNode(9)
root.right.right.left =  TreeNode(10)
root.right.right.right =  TreeNode(11)

zig_zag_print(root)
