"""
Write a python function to find the minimum of two numbers.
assert minimum(1,2) == 1
"""
def minimum(num1, num2):
    """
    This function takes two numbers as arguments and returns the minimum of the two numbers.

    :param num1: The first number
    :param num2: The second number
    :return: The minimum of num1 and num2
    """
    if num1 < num2:
        return num1
    else:
        return num2

assert minimum(1,2) == 1</s>