"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""
import math

def multiply_num(numbers):
    """
    Multiply all the numbers in a list and divide by the length of the list.

    :param numbers: list of numbers
    :return: float
    """
    result = 1
    for number in numbers:
        result *= number
    return result / len(numbers)

assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)