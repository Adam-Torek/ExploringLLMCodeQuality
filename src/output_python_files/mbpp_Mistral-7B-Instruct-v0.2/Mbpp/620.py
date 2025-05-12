"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""
from typing import List


def largest_subset(numbers: List[int]) -> int:
    """
    Find the size of the largest subset of a list of numbers so that every pair is divisible.

    :param numbers: List of integers
    :return: Size of the largest subset
    """
    if not numbers:
        return 0

    numbers.sort()
    current_subset_size = 1
    last_number = numbers[0]

    for number in numbers[1:]:
        if number % last_number == 0:
            current_subset_size += 1
        else:
            last_number = number

    return current_subset_size


if __name__ == "__main__":
    assert largest_subset([1, 3, 6, 13, 17, 18]) == 4
    assert largest_subset([1, 2, 3, 4, 5, 6]) == 6
    assert largest_subset([1, 2, 3, 4, 5, 6, 7]) == 0
    assert largest_subset([1, 2, 3, 4, 5, 6, 8]) == 7
    assert largest_subset([]) == 0
    assert largest_subset([1]) == 1
    assert largest_subset([1, 1]) == 2
    assert largest_subset([1, 1, 1]) == 3
    assert largest_subset([1, 1, 1, 1]) == 4
    assert largest_subset([1, 1, 1, 1, 1]) == 5
    assert largest_subset([1, 1, 1, 1, 1, 1]) == 6
    assert largest_subset([1, 1, 1, 1, 1, 1, 1]) == 7
    assert largest_subset([1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert largest_subset([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert largest_subset([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert largest_subset([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
    assert largest_subset([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 12
    assert largest_subset([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 13
    assert largest_subset([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 14
    assert largest_subset([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert largest_subset([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 16
    assert largest_subset([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 17
    assert largest_subset([1, 1, 1, 1, 1, 1, 1, 1, 1