"""
Write a function to maximize the given two tuples.
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""

def maximize_elements(tuples):
    return sorted(tuples, key=lambda x: (x[0] + x[1], x[0], x[1]), reverse=True)

print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10))))
/python/leetcode/easy/1480_running_sum_of_1d_array.py
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
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
/python/leetcode/easy/1365_how_many_numbers_are_smaller_than_the_current_number.py
"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is,
the number of integers j that satisfy i!= j, and nums[j] < nums[i].

Return an array of the form [num[0], num[1],..., num[n-1]], where num[i] is the number of integers that are smaller
than nums[i].

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

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(1 for x in nums if x < n) for n in nums]
/python/leetcode/easy/1295_find_numbers_with_even_number_of_digits.py
"""
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345