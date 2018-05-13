class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def print(self):
        if self.empty():
            print("Empty")
        else:
            pt = self.head
            print_string = ''
            while pt is not None:
                print_string += '->' + str(pt.value)
                pt = pt.next
            print(print_string)
            print("Head: %s" % (self.head.value))
            print("Tail: %s" % (self.tail.value))
            print("Size: %s" % (self.get_size()))
    def get_size(self):
        if self.empty():
            return 0
        i = 0
        pt = self.head
        while pt != self.tail:
            pt = pt.next
            i += 1
        return i + 1
    def empty(self):
        return self.head is None and self.tail is None
    def value_at(self, index):
        i = 0
        pt = self.head
        while pt is not None:
            if i == index:
                return pt.value
        return None
    def push_front(self, value):
        new_front = Node(value)
        if self.empty():
            self.head = new_front
            self.tail = new_front
        else:
            temp = self.head
            self.head = new_front
            self.head.next = temp
    def push_back(self, value):
        new_back = Node(value)
        if self.empty():
            self.head = new_back
            self.tail = new_back
        else:
            self.tail.next = new_back
            self.tail = new_back
    def pop_front(self):
        if self.empty():
            return None
        elif self.head == self.tail:
            current = self.head
            self.head = None
            self.tail = None
            return current.value
        else:
            old_front = self.head
            self.head = self.head.next
            old_front.next = None
            return old_front.value
    def pop_back(self):
        if self.empty():
            return None
        elif self.head == self.tail:
            current = self.head
            self.head = None
            self.tail = None
            return current.value
        else:
            last = self.head
            current = last.next
            while current != self.tail:
                last = current
                current = current.next
            self.tail = last
            self.tail.next = None
            return current.value
    def front(self):
        if not self.empty():
            return self.head.value
    def back(self):
        if not self.empty():
            return self.tail.value
    def insert(self, index, value):
        if self.empty() or index == 0:
            self.push_front(value)
        elif index > self.get_size() - 1:
            return None
        elif index == self.get_size() - 1:
            self.push_back(value)
        else:
            i = 0
            pt = self.head
            while i < index - 1:
                pt = pt.next
                i += 1
            new_node = Node(value)
            new_node.next = pt.next
            pt.next = new_node
    def erase(self, index):
        if self.empty():
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif index == self.get_size():
            return None
        elif index == 0:
            temp = self.head.next
            self.head.next = None
            self.head = temp
        elif index == self.get_size() - 1:
            last = self.head
            current = last.next
            while current != self.tail:
                last = current
                current = current.next
            self.tail = last
            self.tail.next = None
        else:
            i = 0
            pt = self.head
            while i < index - 1:
                pt = pt.next
                i += 1
            temp = pt.next
            pt.next = temp.next
            temp.next = None
    def value_n_from_end(self, n):
        i = 0
        pt = self.head
        while i < self.get_size() - n - 1:
            pt = pt.next
            i += 1
        return pt.value
    def reverse(self):
        old_head = self.head
        if self.empty() or self.get_size() == 1:
            return None
        elif self.get_size() == 2:
            self.head = self.tail
            self.tail = old_head
        else:
            last = self.head
            current = self.head.next
            front = self.head.next.next
            last.next = None

            while current != self.tail:
                current.next = last

                last = current
                current = front
                front = front.next
            current.next = last
            self.tail = old_head
            self.head = current
    def remove_value(self, value):
        i = 0
        pt = self.head
        while pt is not None:
            if pt.value == value:
                self.erase(i)
                return
            else:
                pt = pt.next
                i += 1
    
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Testing Commands

ll = LinkedList()
ll.insert(0, 3)
ll.print()
ll.insert(0, 1)
ll.print()


ll.push_back(5)
ll.push_front(2)
ll.push_back(9)
ll.push_back(13)
print(ll.front())
print(ll.back())

ll.print()
print(ll.pop_front())
ll.print()
print(ll.pop_back())
ll.print()
print(ll.front())
print(ll.back())
ll.print()

ll.insert(1, 7)
ll.print()

ll.erase(0)
ll.print()

print(ll.value_n_from_end(4))

ll.reverse()
ll.print()
ll.erase(0)
ll.print()

ll.reverse()
ll.print()

ll.erase(0)
ll.erase(0)
ll.print()

ll.erase(0)
ll.print()

for i in range(10):
    ll.push_back(i)
ll.print()

ll.remove_value(5)
ll.print()

ll.remove_value(9)
ll.print()