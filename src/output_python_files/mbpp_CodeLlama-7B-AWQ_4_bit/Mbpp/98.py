"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""

import math


def multiply_num(nums):
    """
    :param nums: list of numbers
    :return: multiplication of all numbers in the list divided by the length of the list
    """
    return sum(nums) / len(nums)


if __name__ == "__main__":
    print(multiply_num((8, 2, 3, -1, 7)))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.0001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.00001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.0000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.00000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.000000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.0000000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.00000000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.000000000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.0000000000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.00000000000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.000000000000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.0000000000000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.00000000000000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.000000000000000001))
    print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.