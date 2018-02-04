class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseandcopy(head):
    revhead = None
    while head != None:
        n = Node(head.val)
        n.next = revhead
        revhead = n
        head = head.next
    return revhead
    
def ispalin(one):
    two = reverseandcopy(head)
    while one != None and two != None:
        if one.val != two.val:
            return False
        one = one.next
        two = two.next
    return True
    

head = Node(9)
n1 = Node(1)
n2 = Node(8)

head.next = n1
n1.next = n2

print( ispalin(head))
