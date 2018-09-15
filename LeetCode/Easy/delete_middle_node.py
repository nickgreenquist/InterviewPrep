# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

# make a simple list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

to_delete = head.next.next # 3

# print list
print("Full List:")
current = head
while current:
    print(current.val)
    current = current.next

# delete a middle node
deleteNode(to_delete)

# print list
print("\nUpdated List:")
current = head
while current:
    print(current.val)
    current = current.next