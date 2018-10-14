'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head):
    last = None
    current = head
    first = current.next
    while first:
        current.next = last
        last = current
        current = first
        first = first.next
    current.next = last
    return current

def reorderList(head):
    if not head or not head.next:
        return
    
    last = None
    slow = head
    fast = head
    while fast:
        last = slow
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            break
            
    last.next = None
    slow = reverse(slow)
    
    # merge lists
    current = head
    while slow:
        next_current = current.next
        next_slow = slow.next
        current.next = slow
        current.next.next = next_current
        
        slow = next_slow
        current = next_current

           
'''
Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
'''
head = ListNode(1)
current = head
for i in range(2, 5):
    current.next = ListNode(i)
    current = current.next

reorderList(head)

current = head
sb = ""
while current:
    sb += str(current.val) + '->'
    current = current.next
print(sb)

'''
Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''   
head = ListNode(1)
current = head
for i in range(2, 6):
    current.next = ListNode(i)
    current = current.next

reorderList(head)

current = head
sb = ""
while current:
    sb += str(current.val) + '->'
    current = current.next
print(sb)   


        