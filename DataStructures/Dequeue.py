class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class MyCircularDeque(object):
    def __init__(self, k):
        self.head = None
        self.tail = None
        self.max = k
        self.size = 0    

    def insertFront(self, value):
        if self.size ==  self.max:
            return False
        elif self.size == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            new_node.next = self.head
            new_node.prev = self.tail
            
            self.head.prev = new_node
            self.tail.next = new_node
            
            self.head = new_node
            
        self.size += 1
        return True
        

    def insertLast(self, value):
        if self.size ==  self.max:
            return False
        elif self.size == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            new_node.next = self.head
            new_node.prev = self.tail
            
            self.head.prev = new_node
            self.tail.next = new_node
            
            self.tail = new_node
            
        self.size += 1
        return True
        

    def deleteFront(self):
        if self.size == 0:
            return False
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.tail.next = self.head.next
            self.head.next.prev = self.tail
            self.head = self.head.next
            
            self.size -= 1
        
        return True

    def deleteLast(self):
        if self.size == 0:
            return False
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head.prev = self.tail.prev
            self.tail.prev.next = self.head
            self.tail = self.tail.prev
            
            self.size -= 1
            
        return True

    def getFront(self):
        if self.size > 0:
            return self.head.val
        return -1
        

    def getRear(self):
        if self.size > 0:
            return self.tail.val
        return -1

    def isEmpty(self):
        return self.size == 0
        

    def isFull(self):
        return self.size == self.max

    def rotate(self, n):
        if self.size > 0:
            if n > 0: # rotate to the right
                for i in range(n):
                    self.head = self.head.prev
                    self.tail = self.tail.prev
            else: # rotate to the left
                for i in range(-n):
                    self.head = self.head.next
                    self.tail = self.tail.next

    def printDeque(self):
        if self.size > 0:
            current = self.head
            sb = ""
            while current != self.tail:
                sb += str(current.val) + '->'
                current = current.next
            sb += str(current.val) + '->'
            print(sb)
        else:
            print("Empty!")

deque = MyCircularDeque(100)
for i in range(20):
    deque.insertLast(i)

deque.printDeque()
deque.rotate(5)
deque.printDeque()
deque.rotate(-10)
deque.printDeque()