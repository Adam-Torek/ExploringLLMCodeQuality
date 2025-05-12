"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""
def opposite_Signs(num1, num2):
    """
    :param num1: an integer
    :param num2: an integer
    :return: True if the given two integers have opposite signs, False otherwise
    """
    return num1 * num2 < 0