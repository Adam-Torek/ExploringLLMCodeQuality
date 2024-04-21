"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""

def centered_hexagonal_number(n):
    return (n**2 + n + 2) * n // 2

print(centered_hexagonal_number(10))
<file_sep>/0001-0500/0220-minimum-average-difference/minimum-average-difference.py
"""
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.

Example 1:

Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
The average difference of index 3 is the minimum average difference so return 3.

Example 2:

Input: nums = [0]
Output: 0
Explanation:
The only index is 0 so return 0.
The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.

Constraints:

n == nums.length
1 <= n <= 105
-105 <= nums[i] <= 105
"""

from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            left[i] = (left[i - 1] + nums[i]) / (i + 1) if i > 0 else nums[i]
        for i in range(n - 1, -1, -1):
            right[i] = (right[i + 1] + nums[i]) / (n - i) if i < n - 1 else nums[i]
        ans = 0
        for i in range(n):
            if abs(left[i] - right[i]) < abs(left[ans] - right[ans]):
                ans = i
        return ans
<file_sep>/0001-0500/0277-find-the-celebrity/find-the-celebrity.py
"""
Suppose you are at a party