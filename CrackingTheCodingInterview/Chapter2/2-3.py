class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteMid(n):
    n.val = n.next.val
    n.next = n.next.next

head = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(0)
n4 = Node(4)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

deleteMid(n2)

while head != None:
    print(head.val)
    head = head.next