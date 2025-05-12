"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""
def number_ctr(string):
    """
    Function to count number of digits in a given string
    :param string: string to check for digits
    :return: int, number of digits in the string
    """
    return sum(1 for char in string if char.isdigit())

assert number_ctr('program2bedone') == 2