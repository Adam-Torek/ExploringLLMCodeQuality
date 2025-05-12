"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""

import math


def multiply_num(nums):
    """
    :param nums: list of numbers
    :return: the multiplication of all the numbers in the list divided by the length of the list
    """
    return sum(nums) / len(nums)


def test_multiply_num():
    assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)


if __name__ == '__main__':
    test_multiply_num()