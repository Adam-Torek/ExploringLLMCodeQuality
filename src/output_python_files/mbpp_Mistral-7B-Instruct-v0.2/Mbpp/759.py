"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""
import re

def is_decimal(num):
    """
    :param num: string
    :return: bool
    """
    pattern = r"^[-+]?[0-9]*\.?[0-9]{1,2}$"
    if re.match(pattern, num):
        return True
    else:
        return False</s>