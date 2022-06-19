'''
3 + ((5+9)*2)
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def express(node):
    if node:
        # check if leaf (i.e. operand)
        if not node.left and not node.right:
            return int(node.val)
        
        # if not leaf, perform expression
        left = express(node.left)
        right = express(node.right)
        if node.val == '+':
            return left + right
        elif node.val == '*':
            return left * right
        elif node.val == '/':
            return left / right
        elif node.val == '-':
            return left - right

root = Node('+')
root.left = Node('3')
root.right = Node('*')
root.right.left = Node('+')
root.right.left.left = Node('5')
root.right.left.right = Node('9')
root.right.right = Node('2')

answer = express(root)
print(answer)