"""
Write a python function to find the maximum of two numbers.
assert maximum(5,10) == 10
"""
def maximum(num1, num2):
    """
    This function takes two numbers as arguments and returns the maximum of the two numbers.

    :param num1: The first number
    :param num2: The second number
    :return: The maximum of the two numbers
    """
    if num1 > num2:
        return num1
    else:
        return num2

assert maximum(5,10) == 10</s>