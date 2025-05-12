"""
Write a python function to find quotient of two numbers (rounded down to the nearest integer).
assert find(10,3) == 3
"""
def find(num1, num2):
    """
    This function takes two numbers as arguments and returns the quotient rounded down to the nearest integer.

    :param num1: The first number
    :param num2: The second number
    :return: The quotient rounded down to the nearest integer
    """
    return int(num1 / num2)