"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""

def count_char_position(string):
    count = 0
    for i in range(len(string)):
        if string[i].lower() == "a"[i]:
            count += 1
    return count

print(count_char_position("xbcefg"))
/python/leetcode/easy/1365_how_many_numbers_are_smaller_than_the_current_number.py
"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is,
for each nums[i] you have to count the number of valid j's such that j!= i and nums[j] < nums[i].
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

def smaller_numbers_than_current(nums):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    count = Counter(nums)
    sorted_count = sorted(count.items(), key=lambda x: x[0])
    sorted_count_dict = dict(sorted_count)
    sorted_count_dict_values = sorted_count_dict.values()
    sorted_count_dict_values_list = list(sorted_count_dict_values)
    sorted_count_dict_values_list_cumsum = [0]
    for i in range(len(sorted_count_dict_values_list)):
        sorted_count_dict_values_list_cumsum.append(sorted_count_dict_values_list_cumsum[i] + sorted_count_dict_values_list[i])
    sorted_count_dict_values_list_cumsum = sorted_count_dict_values_list_cumsum[1:]
    sorted_count_dict_values_list_cumsum_dict = dict(zip(sorted_count_dict.keys(), sorted_count_dict_values_list_cumsum))
    return [sorted_count_dict_values_list_cumsum_dict[i] for i in nums]

print(smaller_numbers_than_current([8,1,2,2,3]))
print(smaller_numbers_than_current([6,5,4,8]))
print(smaller_numbers_than_current([7,7,7,7]))
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

def days_between_dates(date1, date2):
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    date1_year, date1_month, date1_day