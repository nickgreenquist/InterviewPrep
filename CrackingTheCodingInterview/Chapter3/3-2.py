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

class Node():
    def __init__(self, val, min):
        self.val = val
        self.min = min

class MinStack(Stack):
    def __init__(self):
        Stack.__init__(self)

    def push(self, value):
        newMin = min(value, self.getMin())
        super(MinStack, self).push(Node(value, newMin))

    def getMin(self):
        if self.isEmpty():
            return 100000
        else:
            return self.peek().min

ms = MinStack()
ms.push(5)
ms.push(6)
print(ms.getMin()) #should be 5

ms.push(3)
ms.push(7)
print(ms.getMin()) #should be 3

ms.pop()
ms.pop()
print(ms.getMin()) #should be 5