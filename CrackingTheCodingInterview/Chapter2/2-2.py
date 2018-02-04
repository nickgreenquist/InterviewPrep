class Node():
    def __init__(self, val):
        self.next = None
        self.val = val

def ktolast(head, k):
    n = head
    length = 0
    while n != None:
        length += 1
        n = n.next
    print(length)

    length = length - k
    while length != 0:
        length -= 1
        head = head.next
    return head.val


head = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(0)
n4 = Node(4)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

print (ktolast(head, 2))
