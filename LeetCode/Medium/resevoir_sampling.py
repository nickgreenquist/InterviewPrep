from random import randint

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getRandom(head):
    k = 3
    resevoir = [0]*k
    
    # fill up resevoir
    for i in range(k):
        if head:
            resevoir[i] = head
            head = head.next
        else:
            # if not even k items, return random node in resevoir
            r = randint(0, i-1)
            return resevoir[r].val
    
    kth = k
    while head:
        r = randint(0, kth)
        
        if r < k:
            resevoir[r] = head
        
        head = head.next
        kth += 1
    
    r = randint(0, k-1)
    return resevoir[r].val

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)

distribution = [0]*5
for i in range(10000):
    rand_val = getRandom(head)
    distribution[rand_val] += 1
print("0: {}, 1: {}, 2: {}, 3: {}, 4: {}".format(distribution[0], distribution[1], distribution[2], distribution[3], distribution[4]))
