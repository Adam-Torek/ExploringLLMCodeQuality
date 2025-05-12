"""
Write a function to sort the given array by using shell sort.
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
"""

def shell_sort(array):
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array

print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))
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
        while slow!= fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

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
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.