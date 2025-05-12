"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""

def max_sum(arr):
    """
    :param arr: list
    :return: int
    """
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)
    max_sum_arr = [0] * len(arr)
    max_sum_arr[0] = arr[0]
    max_sum_arr[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        max_sum_arr[i] = max(max_sum_arr[i - 1], max_sum_arr[i - 2] + arr[i])
    return max_sum_arr[-1]


if __name__ == '__main__':
    print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]))
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
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        res = 0
        i = 0
        while N > 0:
            if N % 2 == 0:
                res += 2 ** i
            i += 1
            N //= 2
        return res


if __name__ == '__main__':
    print(Solution().bitwiseComplement(5))
<file_sep>/leetcode/1-100/0003. Longest Substring Without Repeating Characters.py
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if