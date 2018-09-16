# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedListSummer(object):
    def getSum(self, head):
        num = 0
        base = 1
        while head:
            num += base * head.val
            head = head.next
            base *= 10
        return num
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        shorter = None
        longer = None
        
        l1_length = 0
        current = l1
        while current:
            l1_length += 1
            current = current.next
        
        l2_length = 0
        current = l2
        while current:
            l2_length += 1
            current = current.next
            
        if l2_length > l1_length:
            longer = l2
            shorter = l1
        else:
            longer = l1
            shorter = l2
            
        current_shorter = shorter
        current_longer = longer
        last_longer = None
        s = 0
        c = 0
        while current_shorter:
            s = current_shorter.val + current_longer.val + c
            if s >= 10:
                c = s // 10
                s = s % 10
            else:
                c = 0
            current_longer.val = s
            
            current_shorter = current_shorter.next
            
            last_longer = current_longer
            current_longer = current_longer.next
        
        current = current_longer
        last = last_longer
        while current:
            s = current.val + c
            if s >= 10:
                c = s // 10
                s = s % 10
            else:
                c = 0
            current.val = s
            
            last = current
            current = current.next
        
        if c > 0:
            node = ListNode(c)
            last.next = node
        
        return self.getSum(longer)

'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 7)
Output: 7 -> 0 -> 1 -> 1
Explanation: 342 + 765 = 1107.
'''
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

summer = LinkedListSummer()
print(summer.addTwoNumbers(l1, l2))