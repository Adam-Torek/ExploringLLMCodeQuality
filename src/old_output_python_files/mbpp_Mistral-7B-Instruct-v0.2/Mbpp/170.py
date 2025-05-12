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