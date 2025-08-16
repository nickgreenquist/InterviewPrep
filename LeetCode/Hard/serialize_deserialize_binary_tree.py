# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def traverse(node):
            if not node:
                return ['N']
            t = []
            t.append(str(node.val))
            t += traverse(node.left)
            t += traverse(node.right)
            return t
        
        ser = traverse(root)
        return ','.join(ser)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ser = data.split(',')

        i = [0]
        def traverse(ser):
            if ser[i[0]] == 'N':
                i[0] += 1
                return None
            node = TreeNode(int(ser[i[0]]))
            i[0] += 1

            node.left = traverse(ser)
            node.right = traverse(ser)

            return node
        
        root = traverse(ser)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

ser = Codec()
deser = Codec()

serialized = ser.serialize(root)
print(serialized)

new_root = deser.deserialize(ser.serialize(root))
serialized = ser.serialize(new_root)
print(serialized)