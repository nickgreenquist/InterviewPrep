class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def findloopsize(n):
    p1 = n
    p2 = n.next
    while p2 != None:
        if p1 == p2:
            break
        p1 = p1.next
        p2 = p2.next.next
    
    #find size of loop
    size = 1
    p2 = p2.next
    while p2 != p1:
        p2 = p2.next
        size += 1
    print(size)

    #set p1 ahead by size
    p1 = n
    p2 = n
    for i in range(size):
        p1 = p1.next
    
    #find intersection node
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1.val



head = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n2

print(findloopsize(head))