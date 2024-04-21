"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""

import math


def multiply_num(nums):
    """
    Multiply all the numbers in a list and divide with the length of the list.
    :param nums: list of numbers
    :return: float
    """
    return sum(nums) / len(nums)


if __name__ == '__main__':
    print(multiply_num((8, 2, 3, -1, 7)))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))
    print(multiply_num((8, 2, 3, -1, 7, 10, 100)))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7, 10, 100)), 1.8, rel_tol=0.001))
    print(multiply_num((8, 2, 3, -1, 7, 10, 100, 1000)))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7, 10, 100, 1000)), 1.8, rel_tol=0.001))
    print(multiply_num((8, 2, 3, -1, 7, 10, 100, 1000, 10000)))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7, 10, 100, 1000, 10000)), 1.8, rel_tol=0.001))
    print(multiply_num((8, 2, 3, -1, 7, 10, 100, 1000, 10000, 100000)))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7, 10, 100, 1000, 10000, 100000)), 1.8, rel_tol=0.001))
    print(multiply_num((8, 2, 3, -1, 7, 10, 100, 1000, 10000, 100000, 1000000)))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7, 10, 100, 1000, 10000, 100000, 1000000)), 1.8, rel_tol=0.001))
    print(multiply_num((8, 2, 3, -1, 7, 10, 100, 1000, 10000, 100000, 1000000, 10000000)))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7, 10, 100, 1000, 10000, 100000, 1000000, 10000000)), 1.8, rel_tol=0.001))
    print(multiply_num((8, 2, 3, -1, 7, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 10000000