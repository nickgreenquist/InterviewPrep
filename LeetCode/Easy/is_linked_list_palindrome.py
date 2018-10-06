'''
Given a singly linked list, determine if it is a palindrome.

Could you do it in O(n) time and O(1) space?
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head):
    if head:
        last = None
        current = head
        next = head.next
        while next:
            current.next = last
            last = current
            current = next
            next = next.next
        current.next = last
        return current

def isPalindrome(head):
    if not head:
        return True
    
    # find middle and sort second half of linked list
    # lock step down the first half and reversed second half, comparing each node's value    
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # reverse the second half
    half2 = reverse(slow)
    half1 = head
    while half1 and half2:
        if half1.val != half2.val:
            return False
        half1 = half1.next
        half2 = half2.next
    return True

'''
Example 1:

Input: 1->2
Output: false
'''
head = ListNode(1)
head.next = ListNode(2)
print(isPalindrome(head))

'''
Example 2:

Input: 1->2->2->1
Output: true
'''
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(isPalindrome(head))