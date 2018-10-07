class Node(object):
    def __init__(self, val, min_seen):
        self.val = val
        self.min = min_seen
        self.next = None
        self.prev = None
        
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.head:
            self.head = Node(x, x)
        else:
            min_seen = min(self.getMin(), x)
            new_head = Node(x, min_seen)
            
            self.head.next = new_head
            new_head.prev = self.head
            self.head = new_head
        

    def pop(self):
        """
        :rtype: void
        """
        if self.head:
            to_pop = self.head
            self.head = self.head.prev
            
            if self.head:
                self.head.next = None
                
            return to_pop
        

    def top(self):
        """
        :rtype: int
        """
        if self.head:
            return self.head.val
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.head:
            return self.head.min
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-1)
obj.pop()

print(obj.getMin()) #-2
print(obj.pop().val) #0
print(obj.getMin()) #-2