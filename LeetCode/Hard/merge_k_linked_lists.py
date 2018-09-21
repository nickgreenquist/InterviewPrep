# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

def mergeKLists(lists):
    heap = []
    current, head = None, None
    while True:
        all_none = True
        for i in range(len(lists)):
            l = lists[i]
            if l:
                all_none = False
                heapq.heappush(heap, (l.val, i))
                lists[i] = lists[i].next
        if all_none and len(heap) < 1:
            break
        val, i = heapq.heappop(heap)
        if not head:
            head = ListNode(val)
            current = head
        else:
            current.next = ListNode(val)
            current = current.next
    return head
'''
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
h1 = ListNode(1)
h1.next = ListNode(4)
h1.next.next = ListNode(5)

h2 = ListNode(1)
h2.next = ListNode(3)
h2.next.next = ListNode(4)

h3 = ListNode(2)
h3.next = ListNode(6)

head = mergeKLists([h1, h2, h3])
current = head
sb = ""
while current:
    sb += str(current.val) + '->'
    current = current.next
print(sb)