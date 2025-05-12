"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""
import re

def check_integer(string):
    """
    Function to check if a string represents an integer or not.
    :param string: string to be checked
    :return: True if string represents an integer, False otherwise
    """
    pattern = re.compile(r'^\+?[0-9]+$')
    return bool(pattern.match(string))