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

def sortStack(s1):
    s2 = Stack()
    while not s1.isEmpty():
        tmp = s1.pop()

        #put things from s2 that are bigger than tmp into s1
        while not s2.isEmpty() and s2.peek() > tmp:
            s1.push(s2.pop())

        #put tmp into the right spot in s2
        s2.push(tmp)

    while not s2.isEmpty():
        s1.push(s2.pop())
    return s1


s1 = Stack()
s1.push(5)
s1.push(10)
s1.push(7)
s1.push(12)
s1.push(8)
s1.push(3)
s1.push(1)

s1 = sortStack(s1)
while not s1.isEmpty():
    n = s1.pop()
    print(n)