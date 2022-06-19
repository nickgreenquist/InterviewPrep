class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.computed = None

def express(node):
    if node:
        # check if leaf (i.e. operand)
        if not node.left and not node.right:
            return int(node.val)
        
        # if already computed, simply return
        if node.computed:
            return node.computed
        
        # perform computation
        left = express(node.left)
        right = express(node.right)
        answer = None
        if node.val == '+':
            answer = left + right
        elif node.val == '*':
            answer = left * right
        elif node.val == '/':
            answer = left / right
        elif node.val == '-':
            answer = left - right
        
        if answer:
            node.computed = answer
            return node.computed


# (2 + (3*4)) + ((3*4) / 6) = 16
root = Node('+')
root.left = Node('+')
root.left.left = Node('2')
root.left.right = Node('*')

root.right = Node('/')
# create DAG: point to same node
root.right.left = root.left.right # Node('*')

root.right.right = Node('6')
root.right.left.left = Node('3')
root.right.left.right = Node('4')

answer = express(root)
print(answer)