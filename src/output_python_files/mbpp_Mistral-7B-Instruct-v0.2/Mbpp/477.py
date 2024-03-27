"""
Write a python function to convert the given string to lower case.
assert is_lower("InValid") == "invalid"
"""
def is_lower(string):
    """
    This function converts the given string to lower case.

    :param string: The string to be converted to lower case.
    :return: The lower case version of the given string.
    """
    return string.lower()

# Test the function
assert is_lower("InValid") == "invalid"
assert is_lower("HeLLo") == "hello"
assert is_lower("123") == "123"
assert is_lower("") == ""</s>