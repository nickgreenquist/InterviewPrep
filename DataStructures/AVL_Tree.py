class Node(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.height = 1

'''
Left Left:
If the violation of the balance comes from the left subtree being too big
The second Left means the left child's left subtree is also higher than its right subtree

Left Right:
If the violation of the balance comes from the left substree being too big
The Right means the left child's right subtree is bigger than it's left subtree

Right Right:
If the violation of the balance comes from the right substree being too big
The second Right means the right child's right subtree is also higher than its left subtree

Right Left
If the violation of the balances comes from the right substree being too big
The Left means the right child's left subtree is bigger than it's right subtree

Goals:
Turn Left Rights -> Left Left
Then Rotate Right

Turn Right Left -> Right Right
The Rotate Left

'''
class AVL_Tree(object):
    def __init__(self):
        self.root = None

    def get_height(self, root):
        if not root:
            return 0
        return root.height
    
    def get_size(self, root):
        if not root:
            return 0
        return root.size

    def rot_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root    

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1

        return new_root

    def rot_right(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1

        return new_root
    
    def _insert(self, root, val):
        if not root:
            return Node(val)
        if val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # Balance the tree if needed
        balance = self.get_height(root.left) - self.get_height(root.right)

        # Left
        if balance > 1:
            # Left
            if self.get_height(root.left.left) >= self.get_height(root.left.right):
                return self.rot_right(root)
            # Right
            else:
                root.left = self.rot_left(root.left)
                return self.rot_right(root)

        # Right
        if balance < -1:
            # Right
            if self.get_height(root.right.right) >= self.get_height(root.right.left):
                return self.rot_left(root)
            # Left
            else:
                root.right = self.rot_right(root.right)
                return self.rot_left(root)

        return root
    
    def insert(self, val):
        root = self.root
        self.root = self._insert(root, val)

# helper functions to get some stats on the tree
def max_depth(root):
    if root:
        return max(max_depth(root.left), max_depth(root.right)) + 1
    else:
        return 0

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

t = AVL_Tree()
for i in range(120):
    t.insert(i)

print(max_depth(t.root))
# print(inorder_traversal(t.root))
print()

t = AVL_Tree()
t.insert(1)
t.insert(2)
t.insert(3)


print(t.root.val)
print(t.root.left.val)

print()

print(t.get_height(t.root))
print(t.get_height(t.root.right))
print(t.get_height(t.root.right.left))