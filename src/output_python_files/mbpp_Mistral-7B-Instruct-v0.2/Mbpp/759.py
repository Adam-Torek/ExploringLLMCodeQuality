"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""
import re

def is_decimal(num):
    """
    :param num: string
    :return: boolean
    """
    pattern = r'^\d+\.?\d{0,2}$'
    return bool(re.match(pattern, num))