class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.size = 0 # num elements in tree including self

# NOTE: not efficient, use Min and Max Heaps instead as core data structure
# NOTE: this is still logn to find median and insert, etc, but not the best
class MedianFinder:

    def __init__(self):
        self.min_tree_root = None
        self.max_tree_root = None
        
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_size(self, root):
        if not root:
            return 0
        return root.size
    
    def getLeftMost(self, root):
        while root.left:
            root = root.left
        return root
    
    def getRightMost(self, root):
        while root.right:
            root = root.right
        return root
    
    def updateSizeAndHeightOfNode(self, root):
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)
    
    def updateSizeFromLeft(self, root):
        if root is None:
            return None
        self.updateSizeFromLeft(root.left)
        self.updateSizeAndHeightOfNode(root)
    
    def updateSizeFromRight(self, root):
        if root is None:
            return None
        self.updateSizeFromRight(root.right)
        self.updateSizeAndHeightOfNode(root)
    
    def getLeftMostAndDelete(self):
        if self.min_tree_root is None:
            return None
        if self.get_size(self.min_tree_root) == 1:
            val_to_return = self.min_tree_root
            self.min_tree_root = None
            return val_to_return
        if self.get_size(self.min_tree_root) == 2:
            val_to_return = self.min_tree_root
            if self.min_tree_root.left is None:
                val_to_return = self.min_tree_root
                self.min_tree_root = self.min_tree_root.right
            else:
                val_to_return = self.min_tree_root.left
            self.min_tree_root.right = None
            self.min_tree_root.left = None
            self.min_tree_root.height = 1
            self.min_tree_root.size = 1
            return val_to_return
            
        root = self.min_tree_root
        parent = self.min_tree_root
        while root.left:
            parent = root
            root = root.left
        parent.left = root.right
        
        self.updateSizeFromLeft(self.min_tree_root)
        return root
    
    def getRightMostAndDelete(self):
        if self.max_tree_root is None:
            return None
        if self.get_size(self.max_tree_root) == 1:
            val_to_return = self.max_tree_root
            self.max_tree_root = None
            return val_to_return
        if self.get_size(self.max_tree_root) == 2:
            val_to_return = self.max_tree_root
            if self.max_tree_root.right is None:
                val_to_return = self.max_tree_root
                self.max_tree_root = self.max_tree_root.left
            else:
                val_to_return = self.max_tree_root.right
            self.max_tree_root.right = None
            self.max_tree_root.left = None
            self.max_tree_root.height = 1
            self.max_tree_root.size = 1
            return val_to_return
            
        root = self.max_tree_root
        parent = self.max_tree_root
        while root.right:
            parent = root
            root = root.right
        parent.right = root.left
        
        self.updateSizeFromRight(self.max_tree_root)
        return root

    def rot_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root    

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)

        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1
        new_root.size = 1 + self.get_size(new_root.left) + self.get_size(new_root.right)

        return new_root

    def rot_right(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)

        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1
        new_root.size = 1 + self.get_size(new_root.left) + self.get_size(new_root.right)

        return new_root
    
    def _insert(self, root, val):
        if not root:
            new_node = Node(val)
            new_node.size = 1
            return new_node
        if val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)
        
        # update height and size
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)

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
    
    def insertMinTree(self, val):
        root = self.min_tree_root
        self.min_tree_root = self._insert(root, val)
        
    def insertMaxTree(self, val):
        root = self.max_tree_root
        self.max_tree_root = self._insert(root, val)

    def addNum(self, num: int) -> None:
        # add the number to the min tree
        self.insertMinTree(num)
        
        # get the smallest number from the min heap (middle value)
        smallest_from_min_tree = self.getLeftMostAndDelete().val
        
        # add to the max tree
        self.insertMaxTree(smallest_from_min_tree)
        
        # if min tree smaller than max tree
        if self.get_size(self.min_tree_root) < self.get_size(self.max_tree_root):
            largest_from_max = self.getRightMostAndDelete().val
            
            # insert to min tree
            self.insertMinTree(largest_from_max)
        

    def findMedian(self) -> float:
        
        # if min tree is bigger than max tree
        if self.get_size(self.min_tree_root) > self.get_size(self.max_tree_root):
            smallest_from_min_tree = self.getLeftMost(self.min_tree_root).val
            return smallest_from_min_tree
        
        # median is the average of the middle two values
        smallest_from_min_tree = self.getLeftMost(self.min_tree_root).val
        max_from_max_tree = self.getRightMost(self.max_tree_root).val
        return (smallest_from_min_tree + max_from_max_tree) / 2.0