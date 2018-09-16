# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    lookup = {}
    i = 0
    current = head
    while current:
        lookup[i] = current
        current = current.next
        i += 1
    to_remove_i = (i-1) - (n-1)
    to_remove = lookup[to_remove_i]
    if to_remove != head:
        prev = lookup[to_remove_i - 1]
        prev.next = to_remove.next
    else:
        head = head.next
    return head

head = ListNode(1)
current = head
for i in range(2, 6):
    current.next = ListNode(i)
    current = current.next

head = removeNthFromEnd(head, 2)
current = head
while current:
    print(current.val)
    current = current.next