# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeSort(head):
    if head and head.next:
        
        # find the middle
        mid = None
        slow = head
        fast = head
        while fast and fast.next:
            mid = slow
            slow = slow.next
            fast = fast.next.next
        
        # cut off the list at the midpoint (very important)
        mid.next = None
        
        # sort both lists and merge
        left = mergeSort(head)
        right = mergeSort(slow)    
        return merge(left, right)
    else:
        return head
    
def merge(left, right):

    # find best new head
    head = None
    if left.val < right.val:
        head = left
        left = left.next
    else:
        head = right
        right = right.next
    
    # merge node by node to new head
    current = head
    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
        
    # append the leftover segments if needed
    if left:
        current.next = left
    elif right:
        current.next = right

    return head

# create test linked list and sort it
head = ListNode(4)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head = mergeSort(head)

# verify the list is sorted
str_buidler = ""
current = head
while current:
    str_buidler += str(current.val) + '->'
    current = current.next
print(str_buidler)