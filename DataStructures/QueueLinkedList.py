class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def empty(self):
        return self.head is None and self.tail is None
    def enqueue(self, value):
        if self.empty():
            self.head = Node(value)
            self.tail = self.head
        else:
            new_head = Node(value)
            new_head.next = self.head
            self.head = new_head
    def dequeue(self):
        if self.empty():
            return None
        elif self.head == self.tail:
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        else:
            last = self.head
            pt = last.next
            while pt != self.tail:
                last = pt
                pt = pt.next
            last.next = None
            self.tail = last
            return pt.value

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Test calls
q = Queue()
for i in range(1, 10):
    q.enqueue(i)

val = q.dequeue()
while val:
    print(val)
    val = q.dequeue()
            