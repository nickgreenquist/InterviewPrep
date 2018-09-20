# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenList(head):
    # None list
    if not head:
        return None
    # size one list
    if not head.next:
        return head
    # size two list
    if not head.next.next:
        return head
    
    # actually do hard stuff
    last = head
    first_even = head.next
    current = last.next
    tail = current.next
    while tail:
        last.next = tail
        current.next = tail.next
        tail.next = first_even
        last = last.next
        
        current = current.next
        
        # have to check this for odd sized lists
        if not current:
            break
            
        tail = current.next
    
    return head
               
head = ListNode(1)
current = head
for i in range(2, 26):
    current.next = ListNode(i)
    current = current.next

head = oddEvenList(head)
builder = ""
while head:
    builder += str(head.val) + "->"
    head = head.next
print(builder)

