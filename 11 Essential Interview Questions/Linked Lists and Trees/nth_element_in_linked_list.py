class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def nth_from_end(head, n):
    if n < 1:
        return None

    tortoise = head
    hare = head
    
    # give hare headstart of size n
    for i in range(n):
        if hare:
            hare = hare.next
        else:
            return None
    
    # move one by one until hare hits None
    while hare:
        tortoise = tortoise.next
        hare = hare.next
    return tortoise.val

head = Node(5)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print(nth_from_end(head, 1))
    
        