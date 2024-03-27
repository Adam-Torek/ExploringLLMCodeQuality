"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""

def zero_count(arr):
    count = 0
    for i in arr:
        if i == 0:
            count += 1
    return count / len(arr)

print(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]))
<file_sep>/python/leetcode/easy/1365_how_many_numbers_are_smaller_than_the_current_number.py
"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j!= i and nums[j] < nums[i].

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

from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        return [sum(count.values()[:i]) for i in nums]

print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))
print(Solution().smallerNumbersThanCurrent([6,5,4,8]))
print(Solution().smallerNumbersThanCurrent([7,7,7,7]))
<file_sep>/python/leetcode/easy/1480_running_sum_of_1d_array.py
"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

class Solution:
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums[:i+1]) for i in range(len(nums))]

print(Solution().runningSum([1,2,3,4]))
print(Solution().runningSum([1,1,1,1,1