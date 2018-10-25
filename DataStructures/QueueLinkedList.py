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
            new_tail = Node(value)
            self.tail.next = new_tail
            self.tail = new_tail
    def dequeue(self):
        if self.empty():
            return None
        else:
            val = self.head.value
            self.head = self.head.next
            return val

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
            