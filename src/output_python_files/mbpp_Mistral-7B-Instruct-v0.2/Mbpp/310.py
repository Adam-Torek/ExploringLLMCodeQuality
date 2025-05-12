"""
Write a function to convert a given string to a tuple of characters.
assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
"""
def string_to_tuple(string):
    """
    Converts a given string to a tuple of characters.
    :param string: The string to be converted to a tuple.
    :return: A tuple of characters.
    """
    return tuple(string)

# Test the function
assert string_to_tuple("python 3.0") == ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')