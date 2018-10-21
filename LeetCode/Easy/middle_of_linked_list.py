# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

# build and print a test linked list
head = ListNode(1)
current = head
sb = ""
for i in range(2, 10):
    sb += str(current.val) + '->'
    current.next = ListNode(i)
    current = current.next
print(sb)

print("Middle node: {}".format(middleNode(head).val))