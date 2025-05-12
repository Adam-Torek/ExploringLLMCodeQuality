"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""

def tuple_intersection(tuple_list):
    """
    :param tuple_list: list of tuples
    :return: set of tuples
    """
    return set.intersection(*tuple_list)


if __name__ == '__main__':
    print(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)]))
    print(tuple_intersection([(5, 4), (3, 4), (6, 5), (9, 11)]))
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


def running_sum(nums):
    """
    :param nums: list of integers
    :return: list of integers
    """
    return [sum(nums[:i + 1]) for i in range(len(nums))]


if __name__ == '__main__':
    print(running_sum([1, 2, 3, 4]))
    print(running_sum([1, 1, 1, 1, 1]))
    print(running_sum([3, 1, 2, 10, 1]))
/python/leetcode/easy/1295_find_numbers_with_even_number_of_digits.py
"""
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""


def find_numbers(nums):
    """
    :param nums: list of integers
    :return: integer
    """
    return sum(len(str(num)) % 2 == 0 for num in nums)


if __name__ == '__main__':
    print(find_numbers([12, 345, 2, 6, 7896]))
    print(find_numbers([555, 901, 482, 1771]))
/python/leetcode/easy/1281_subtract_the_product_and_sum_of_digits_of_an