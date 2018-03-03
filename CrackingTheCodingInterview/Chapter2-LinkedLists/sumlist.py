class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def sumlist(n1, n2):
    solution = Node(0)
    front = solution
    while n1 != None and n2 != None:
        sum = n1.val + n2.val
        remainder = sum % 10
        sum = int(sum / 10)
        solution.val = solution.val + remainder
        newNode = Node(sum)
        solution.next = newNode

        n1 = n1.next
        n2 = n2.next
        solution = solution.next
    return front


one_head = Node(9)
one1 = Node(9)
one2 = Node(9)

one_head.next = one1
one1.next = one2

two_head = Node(9)
two1 = Node(9)
two2 = Node(9)

two_head.next = two1
two1.next = two2

head = sumlist(one_head, two_head)
while head != None:
    print(head.val)
    head = head.next
