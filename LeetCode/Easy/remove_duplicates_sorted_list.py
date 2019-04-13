'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    if not head:
        return head
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

'''
Input: 1->1->2->3->3
Output: 1->2->3
'''
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
head = deleteDuplicates(head)

current = head
while current:
    print(current.val)
    current = current.next


