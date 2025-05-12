"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""

def largest_subset(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    nums.sort()
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(largest_subset([ 1, 3, 6, 13, 17, 18 ]))/leetcode/1000-1099/1000.py
"""
Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
Return 0 if S is odd, otherwise return 1.

Example 1:
Input: [34,23,1,24,75,33,54,8]
Output: 0
Explanation:
The minimal element is 1, and the sum of those digits is S = 1 which is odd, so the answer is 0.

Example 2:
Input: [99,77,33,66,55]
Output: 1
Explanation:
The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.

Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
"""

class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return 0 if sum(map(int, str(min(A)))) % 2 else 1

print(Solution().sumOfDigits([34,23,1,24,75,33,54,8]))/leetcode/1-99/10.py
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        max_len = 1
        start = 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
        return s[start:start + max_len]

print(Solution().longestPalindrome("babad"))/leetcode/1-99/11.py
"""
Given n non-negative integers a1, a2,..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len