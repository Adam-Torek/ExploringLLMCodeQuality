"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""
def sum_negativenum(numbers):
    """
    Calculate the sum of negative numbers in a given list of numbers.

    :param numbers: list of numbers
    :return: int, the sum of negative numbers
    """
    negative_numbers = [num for num in numbers if num < 0]
    return sum(negative_numbers)

assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32</s>