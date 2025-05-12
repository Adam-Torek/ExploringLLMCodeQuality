"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""

def count_Pairs(lst, n):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]!= lst[j]:
                count += 1
    return count

print(count_Pairs([1,2,1],3))
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
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow!= fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

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
head.next.next.next.