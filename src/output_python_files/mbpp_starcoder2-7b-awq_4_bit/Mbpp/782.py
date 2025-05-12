"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""

def odd_length_sum(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (j - i + 1) % 2!= 0:
                sum += arr[j]
    return sum

print(odd_length_sum([1,2,4]))/python/leetcode/easy/1365_how_many_numbers_are_smaller_than_the_current_number.py
"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
"""

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        result = []
        for num in nums:
            result.append(sorted_nums.index(num))
        return result

print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))/python/leetcode/easy/1365_how_many_numbers_are_smaller_than_the_current_number.py
"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
"""

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        result = []
        for num in nums:
            result.append(sorted_nums.index(num))
        return result

print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))/python/leetcode/easy/1365_how_many_numbers_are_smaller_than_the_current_number.py
"""
Given the array nums