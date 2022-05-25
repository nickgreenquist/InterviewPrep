class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def print_dll(head):
    s = []
    while head:
        s.append(str(head.val))
        head = head.next
    print('->'.join(s))

def convert(node):
    if node is None:
        return None, None
    
    left_head, left_tail = convert(node.left)
    list_node = ListNode(node.val)
    right_head, right_tail = convert(node.right)

    list_node.prev = left_tail
    list_node.next = right_head

    if left_tail:
        left_tail.next = list_node
    if right_head:
        right_head.prev = list_node

    head = list_node
    tail = list_node
    if left_head:
        head = left_head
    if right_tail:
        tail = right_tail

    return head, tail


head1 = Node(5)
head1.left = Node(2)
head1.left.left = Node(1)
head1.left.right = Node(3)
head1.right = Node(8)
head1.right.left = Node(6)

# Expected DLL:
# 1-2-3-5-6-8
head, tail = convert(head1)
print_dll(head)