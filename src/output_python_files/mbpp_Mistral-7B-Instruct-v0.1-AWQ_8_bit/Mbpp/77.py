"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""

def is_divisible_by_11(num):
    """
    :param num: int
    :return: bool
    """
    if num % 11 == 0:
        return True
    else:
        return False