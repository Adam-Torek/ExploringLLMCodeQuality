"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""


def sum_range_list(nums, start, end):
    """
    :param nums: list of numbers
    :param start: start index
    :param end: end index
    :return: sum of numbers in the list within the range
    """
    if start < 0 or end < 0 or start > end:
        return 0
    return sum(nums[start:end + 1])


if __name__ == '__main__':
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 8, 10))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 10))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 1))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 12))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 13))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 14))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 15))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 16))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 17))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 18))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 19))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 20))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 21))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 22))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 23))
    print(sum_range_list([2, 1,