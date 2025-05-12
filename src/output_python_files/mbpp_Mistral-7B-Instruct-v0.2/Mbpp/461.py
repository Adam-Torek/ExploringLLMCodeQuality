"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""
def upper_ctr(string):
    """
    This function takes a string as an argument and returns the count of uppercase characters in the string.
    """
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count

# Test the function
assert upper_ctr('PYthon') == 1
assert upper_ctr('The Quick Brown Fox') == 3
assert upper_ctr('') == 0
assert upper_ctr('AaBbCc') == 3
assert upper_ctr('12345') == 0