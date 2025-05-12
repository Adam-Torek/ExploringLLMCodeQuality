"""
The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
"""

def count_same_pair(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1
    return count

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]))
/python/leetcode/easy/1365_how_many_numbers_are_smaller_than_the_current_number.py
"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is,
the number of valid j's such that j!= i and nums[j] < nums[i].

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

def smallerNumbersThanCurrent(nums):
    count = Counter(nums)
    count = sorted(count.items(), key=lambda x: x[0])
    res = []
    for i in range(len(count)):
        if i == 0:
            res.append(0)
        else:
            res.append(res[i-1] + count[i][1])
    return res

print(smallerNumbersThanCurrent([8,1,2,2,3]))
print(smallerNumbersThanCurrent([6,5,4,8]))
print(smallerNumbersThanCurrent([7,7,7,7]))
/python/leetcode/easy/1360_number_of_days_between_two_dates.py
"""
Write a program to count the number of days between two dates.
The two dates are given as strings of the form YYYY-MM-DD.

Example 1:
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

Constraints:
The given dates are valid dates between the years 1971 and 2100.
"""

def daysBetweenDates(date1, date2):
    def get_days(year, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            if year % 4 == 0:
                return 29
            else:
                return 28
        else:
            return 0

    def get_days