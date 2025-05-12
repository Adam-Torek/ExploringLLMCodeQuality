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
/python/leetcode/easy/1365_how_many_numbers_are_smaller_than_the_current_number.py
"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, the number of integers j that satisfy nums[j] < nums[i] where 0 <= j < i.

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
        return [sum(i < j for j in nums) for i in nums]

print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))
print(Solution().smallerNumbersThanCurrent([6,5,4,8]))
print(Solution().smallerNumbersThanCurrent([7,7,7,7]))
/python/leetcode/easy/1360_number_of_days_between_two_dates.py
"""
Write a program to count the number of days between two dates.
The two dates are given as strings of the format YYYY-MM-DD.

Example 1:
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

Constraints:
The given dates are valid dates between the years 1971 and 2100.
"""

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def days_in_month(year, month):
            if month in (1, 3, 5, 7, 8, 10, 12):
                return 31
            elif month == 2:
                if year % 4 == 0 and (year % 100!= 0 or year % 400 == 0):
                    return 29
                else:
                    return 28
            else:
                return 30

        def days_between_dates(year1, month1, day1, year2, month2, day2):
            days = 0
            while year1 < year2 or (year1 == year2 and month1 < month2) or (year1 == year2 and month1 == month2 and day1 < day2):
                days += days_in_month(year1, month1)
                day1 += 1
                if day1 > days_in_month(year1, month1):
                    day1