"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""

def odd_values_string(string):
    """
    :param string: input string
    :return: string with characters removed which have odd index values
    """
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i]
    return new_string


# Test the function
assert odd_values_string('abcdef') == 'ace'