class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    if not head:
        return None
    last = None
    current = head
    n = current.next
    while n:
        current.next = last
        last = current
        current = n
        n = n.next
    current.next = last
    return current

def printList(head):
    current = head
    sb = ""
    while current:
        sb += str(current.val) + '->'
        current = current.next
    print(sb)

head = ListNode(0)
current = head
for i in range(1, 10):
    current.next = ListNode(i)
    current = current.next
# print OG list
printList(head)

# reverse and print
head = reverseList(head)
printList(head)