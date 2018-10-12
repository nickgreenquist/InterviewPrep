class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse(head):
    if not head or not head.next:
        return head
    
    last = None
    current = head
    front = head.next
    while front:
        current.next = last
        last = current
        current = front
        front = front.next
    current.next = last
    return current

def reverse_last_n(head, n):
    if n <= 1:
        return head

    first_half = 0
    length = 0
    slow = head
    fast = head
    while fast:
        slow = slow.next
        first_half += 1
    
        if fast.next:
            fast = fast.next.next
            length += 2
        else:
            length += 1
            break

    if n >= length:
        return reverse(head)

    # must start the reverse from node in first half
    if n > length - first_half:
        last = None
        current = head
        dist = length - n
    else: # get slow up to (length - n) node
        last = None
        current = slow
        dist = (length - first_half) - n

    # find the right start of sub list to reverse and keep track of last
    for i in range(dist):
        last = current
        current = current.next

    last.next = reverse(current)
    return head

def printList(head):
    current = head
    sb = ""
    while current:
        sb += str(current.val) + '->'
        current = current.next
    print(sb)

head = Node(1)
current = head
for i in range(2, 10):
    current.next = Node(i)
    current = current.next

printList(head)
head = reverse_last_n(head, 5)
printList(head)

