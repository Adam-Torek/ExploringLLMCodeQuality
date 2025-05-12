"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""
def big_diff(numbers):
    """
    This function takes a list of numbers as an argument and returns the difference between the largest and smallest number in the list.

    :param numbers: list of numbers
    :return: int, the difference between the largest and smallest number in the list
    """
    if not numbers:
        raise ValueError("The list is empty")

    min_num = min(numbers)
    max_num = max(numbers)

    return max_num - min_num