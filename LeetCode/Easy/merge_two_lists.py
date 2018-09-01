# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    # base cases
    if not l1 and not l2:
        return None
    if l1 and not l2:
        return l1
    if l2 and not l1:
        return l2
    
    # find the best head node
    if l1.val < l2.val:
        best = l1
        l1 = l1.next
    else:
        best = l2
        l2 = l2.next 
    front = best
        
    # main merging logic
    while l1 and l2:
        if l1.val < l2.val:
            best.next = l1
            best = l1
            l1 = l1.next
        else:
            best.next = l2
            best = l2
            l2 = l2.next
            
    # clean up the rest
    if l1:
        best.next = l1
    else:
        best.next = l2
    
    return front

'''
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

merged = mergeTwoLists(l1, l2)
while merged:
    print(merged.val)
    merged = merged.next