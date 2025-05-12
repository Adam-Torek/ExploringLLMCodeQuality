"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""
def sum_range_list(numbers, start, end):
    """
    Function to find the sum of numbers in a list within a range specified by two indices
    :param numbers: list of numbers
    :param start: index of the first number to include in the sum
    :param end: index of the last number to include in the sum
    :return: sum of numbers in the list within the specified range
    """
    if start < 0 or end > len(numbers) or start > end:
        raise IndexError("Invalid indices")
    sum = 0
    for i in range(start, end+1):
        sum += numbers[i]
    return sum

# Test the function
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
assert sum_range_list([], 0, 1) == 0
assert sum_range_list([1,2,3], 1, 3) == 6
assert sum_range_list([1,2,3], 0, 2) == 6
assert sum_range_list([1,2,3], 0, 4) == 10
assert sum_range_list([1,2,3], 4, 0) == 0
assert sum_range_list([1,2,3], 4, 5) == 12
assert sum_range_list([1,2,3], 5, 4) == 0
assert sum_range_list([1,2,3], 10, 10) == 3
assert sum_range_list([1,2,3], 10, 11) == 4
assert sum_range_list([1,2,3], 11, 10) == 0
assert sum_range_list([1,2,3], 11, 12) == 3
assert sum_range_list([1,2,3], 12, 11) == 0
assert sum_range_list([1,2,3], 12, 13) == 0
assert sum_range_list([1,2,3], -1, 1) == 6
assert sum_range_list([1,2,3], -1, 2) == 6
assert sum_range_list([1,2,3], -1, 3) == 6
assert sum_range_list([1,2,3], -1, 4) == 6
assert sum_range_list([1,2,3], -1, 5) == 6
assert sum_range_list([1,2,3], -1, 6) == 6
assert sum_range_list([1,2,3], -1, 7) == 6
assert sum_range_list([1,2,3], -1, 8) == 6
assert sum_range_list([1,2,3], -1, 9) == 6
assert sum_range_list([1,2,3], -1, 10) == 6
assert sum_range_list([1,2,3], -1, 11) == 6
assert sum_range_list([1,2,3], -1, 12) == 6
assert sum_range_list([1,2,3], -2, 1) == 6
assert sum_range_list([1,2,3], -2, 2) == 6
assert sum_range_list([1,2,3], -2, 3) == 6
assert sum_range_list([1,2,3], -2, 4) == 6
assert sum_range_list([1,2,3], -2, 5) == 6
assert sum_range_list([1,2,3], -2, 6) == 6
assert sum_range_list([1,2,3], -2, 7)