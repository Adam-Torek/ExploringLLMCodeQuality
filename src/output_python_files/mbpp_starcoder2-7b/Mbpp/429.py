"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""

def and_tuples(tup1, tup2):
    """
    >>> and_tuples((10, 4, 6, 9), (5, 2, 3, 3))
    (0, 0, 2, 1)
    """
    return tuple(a & b for a, b in zip(tup1, tup2))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/leetcode/0001_two_sum.py
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num + num2 == target:
                    return [i, i+j+1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/leetcode/0002_add_two_numbers.py
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        curr = head
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry /= 10
        return head.next

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/leetcode/0003_longest_substring_without_repeating_characters.py
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_len = 1
        curr_len = 1
        curr_set = set()
        curr_set.add(s[0])
        for i in range(1, len(s)):
            if s[i] not in curr_set:
                curr_len += 1
                curr_set.add(s[i])
            else:
                if curr_len > max_len:
                    max_len