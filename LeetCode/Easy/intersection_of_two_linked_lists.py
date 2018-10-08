# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    
    # check if they intersect at all while capturing the length of each
    currentA = headA
    lengthA = 0
    currentB = headB
    lengthB = 0
    
    # traverse to the last node in A
    lastA = None
    while currentA:
        lastA = currentA
        currentA = currentA.next
        lengthA += 1
    
    # traverse to the last node in B
    lastB = None
    while currentB:
        lastB = currentB
        currentB = currentB.next
        lengthB += 1
        
    # if they dont' share the same last node, they don't intersect ever
    if lastA != lastB:
        return None
    
    # we need to know which is the longer and which is the shorter
    if lengthA > lengthB:
        large = headA
        small = headB
    else:
        large = headB
        small = headA
        
    # move up the long one by diff in length of small and large
    diff_length = abs(lengthA - lengthB)
    current_large = large
    for i in range(diff_length):
        current_large = current_large.next
    
    # find the actual intersection node by moving in lockstep
    current_small = small
    while current_small != current_large:
        current_small = current_small.next
        current_large = current_large.next
    
    return current_small

'''
For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.
'''

headA = ListNode('a1')
headA.next = ListNode('a2')
headA.next.next = ListNode('c1')
headA.next.next.next = ListNode('c2')
headA.next.next.next.next = ListNode('c3')

headB = ListNode('b1')
headB.next = ListNode('b2')
headB.next.next = ListNode('b3')
headB.next.next.next = headA.next.next # ListNode('c1')

intersection = getIntersectionNode(headA, headB)
if intersection:
    print("Intersection: {}".format(intersection.val))
else:
    print("No Intersection!")