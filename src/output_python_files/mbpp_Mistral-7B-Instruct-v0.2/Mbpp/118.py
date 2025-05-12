"""
Write a function to convert a string to a list of strings split on the space character.
assert string_to_list("python programming")==['python','programming']
"""
def string_to_list(string):
    """
    Converts a string to a list of strings split on the space character.

    :param string: The string to be converted to a list.
    :return: A list of strings.
    """
    return string.split()