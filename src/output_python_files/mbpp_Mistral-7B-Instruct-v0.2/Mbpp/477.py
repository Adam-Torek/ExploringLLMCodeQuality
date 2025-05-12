"""
Write a python function to convert the given string to lower case.
assert is_lower("InValid") == "invalid"
"""
def is_lower(string):
    """
    This function converts the given string to lower case.

    :param string: string to be converted to lower case
    :return: lower case string
    """
    return string.lower()

assert is_lower("InValid") == "invalid"