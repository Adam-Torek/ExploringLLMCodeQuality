"""
Write a python function to convert a given string to uppercase.
assert is_upper("person") =="PERSON"
"""
def is_upper(string):
    """
    This function converts the given string to uppercase and returns it.

    Args:
        string: The given string to be converted to uppercase.

    Returns:
        The uppercase version of the given string.
    """
    return string.upper()

# Test the function
assert is_upper("person") == "PERSON"
assert is_upper("Python") == "PYTHON"
assert is_upper("hello") == "HELLO"