"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""

def count_Set_Bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

print(count_Set_Bits(2))
/python/leetcode/easy/141_linked_list_cycle.py
"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

# Test
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next.next.next = ListNode(10)
head.next.next.next.next.next.next.next.next.next.next = ListNode(11)
head.next.next.next.next.next.next.next.next.next.next.next = ListNode(12)
head.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(13)
head.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(14)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(15)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(16)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(17)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(18)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(19)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(20)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(21)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(22)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(23)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(24)
head.next.next.next.next.next.next.next.next.next.next