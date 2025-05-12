"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""
def upper_ctr(string):
    """
    Function to count the number of uppercase characters in a given string
    :param string: string to check
    :return: int, number of uppercase characters in the string
    """
    return sum(1 for char in string if char.isupper())

# Test the function
assert upper_ctr('PYthon') == 1
assert upper_ctr('The quick brown fox jumps over the lazy dog') == 3
assert upper_ctr('') == 0
assert upper_ctr('12345') == 0
assert upper_ctr('ABCDEFG') == 7