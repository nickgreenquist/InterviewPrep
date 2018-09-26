class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycleStart(head):
    if not head:
        return None
    if head.next == head:
        return head
    
    turtle = head
    hare = head
    while turtle and hare:
        turtle = turtle.next
        if hare.next:
            hare = hare.next.next
        else:
            return None
        
        # check if they caught up
        if turtle == hare:
            break
        
    # check if they didn't simply run out of the list
    if not (turtle and hare):
        return None
    
    turtle = head
    while turtle != hare:
        turtle = turtle.next
        hare = hare.next
    return turtle

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next # create cycle on second element (2)

cycle_start = detectCycleStart(head)
if cycle_start:
    print(cycle_start.val)