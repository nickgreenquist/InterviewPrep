# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    # find the first 0
    current = head
    first_zero = None
    while current is not None:
        if current.val == 0:
            first_zero = current
            break
        current = current.next

    running_sum = 0
    last = first_zero
    current = first_zero.next
    while current is not None:
        if current.val == 0:
            last.val = running_sum
            last.next = current.next
            last = current.next
            running_sum = 0
        else:
            running_sum += current.val
        
        current = current.next
    return head

'''
Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.
'''
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(0)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(0)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next = ListNode(0)

# print linked list as single string
vals = []
current = head
while current is not None:
    vals.append(current.val)
    current = current.next

print(vals)
print()

# print linked list after merging
head = mergeNodes(head)
vals = []
current = head
while current is not None:
    vals.append(current.val)
    current = current.next
print(vals)
