class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.items)

def TOH(n, a, b, c):
    if n == 1:
        b.push(a.pop())
    else:
        TOH(n-1, a,c,b)
        b.push(a.pop())
        TOH(n-1, c, b, a)

a = Stack()
a.push(5)
a.push(4)
a.push(3)
a.push(2)
a.push(1)

b = Stack()
c = Stack()

TOH(a.size(),a,b,c)

while not b.isEmpty():
    print(b.pop())

