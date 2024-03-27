"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""

def next_smallest_palindrome(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 10:
        return n + 1
    n_str = str(n)
    n_len = len(n_str)
    if n_len % 2 == 0:
        mid = n_len // 2
        left = n_str[:mid]
        right = n_str[mid:]
        if left == right[::-1]:
            return int(left + right)
        else:
            left = int(left) + 1
            return int(str(left) + str(left)[::-1])
    else:
        mid = n_len // 2
        left = n_str[:mid]
        right = n_str[mid + 1:]
        if left == right[::-1]:
            return int(left + right)
        else:
            left = int(left) + 1
            return int(str(left) + str(left)[::-1])


if __name__ == '__main__':
    print(next_smallest_palindrome(99))
<file_sep>/leetcode/1001-1100/1009. Complement of Base 10 Integer.py
"""
Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.



Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.


Note:

0 <= N < 10^9
"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        n_str = bin(N)[2:]
        n_len = len(n_str)
        res = ''
        for i in range(n_len):
            if n_str[i] == '1':
                res += '0'
            else:
                res += '1'
        return int(res, 2)


if __name__ == '__main__':
    print(Solution().bitwiseComplement(5))
<file_sep>/leetcode/1-100/002. Add Two Numbers.py
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l