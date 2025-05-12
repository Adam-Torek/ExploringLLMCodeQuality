"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""


def sum_range_list(lst, start, end):
    """
    :param lst: list of numbers
    :param start: start index
    :param end: end index
    :return: sum of numbers in a list within a range specified by two indices
    """
    return sum(lst[start:end + 1])


if __name__ == '__main__':
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 8, 10))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 0, 10))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 0, 1))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 1))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 2))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 3))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 4))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 5))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 6))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 7))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 8))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 9))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 10))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 11))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 1, 12))
    print(sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8,