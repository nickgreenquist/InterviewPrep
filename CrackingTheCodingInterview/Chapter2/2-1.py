class Node():
    def __init__(self, val):
        self.next = None
        self.val = val

def removedups(head):
    seen = set()
    front = head
    prev = None
    while head != None:
        if head.val in seen:
            prev.next = head.next
        else:
            seen.add(head.val)
            prev = head
        head = head.next
    return front




head = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(0)
n4 = Node(4)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

head = removedups(head)
while head != None:
    print(head.val)
    head = head.next
