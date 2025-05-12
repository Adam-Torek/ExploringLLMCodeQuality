"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""

def lps(s):
    """
    :param s: string
    :return: int
    """
    pass

if __name__ == '__main__':
    print(lps("TENS FOR TENS"))
<file_sep>/src/leetcode/100_same_tree.py
"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    """
    :param p: TreeNode
    :param q: TreeNode
    :return: bool
    """
    pass

if __name__ == '__main__':
    pass
<file_sep>/src/leetcode/100_two_sum.py
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def two_sum(nums, target):
    """
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """
    pass

if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
<file_sep>/src/leetcode/100_reverse_integer.py
"""
Given a 32-bit signed integer, reverse digits of an integer.
"""

def reverse(x):
    """
    :param x: int
    :return: int
    """
    pass

if __name__ == '__main__':
    print(reverse(123))
<file_sep>/src/leetcode/100_remove_duplicates_from_sorted_array.py
"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

def remove_duplicates(nums):
    """
    :param nums: List[int]
    :return: int
    """
    pass

if __name__ == '__main__':
    print(remove_duplicates([1, 1, 2]))
<file_sep>/src/leetcode/100_longest_common_prefix.py
"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

def longest_common_prefix(strs):
    """
    :param strs: List[str]
    :return: str
    """
    pass

if __name__ == '__main__':
    print(longest_common_prefix(["flower","flow","flight"]))
<file_sep>/src/leetcode/100_valid_parentheses.py
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

def is_valid(s):
    """
    :param s: str
    :return: bool
    """
    pass

if __name__ == '__main__':
    print(is_valid("()"))
<file_sep>/src/leetcode/100_merge_two_sorted_lists.py
"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    """
    :param l1: ListNode
    :param l2: ListNode
    :return: ListNode
    """
    pass

if __name__ == '__main__':
    pass
<file_sep>/src/leetcode/100_remove_element.py
"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.