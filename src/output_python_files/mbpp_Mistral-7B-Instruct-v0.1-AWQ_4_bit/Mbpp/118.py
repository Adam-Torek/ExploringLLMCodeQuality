"""
Write a function to convert a string to a list of strings split on the space character.
assert string_to_list("python programming")==['python','programming']
"""

def string_to_list(string):
    """
    This function takes a string as an input and returns a list of strings split on the space character.
    """
    # split the string on the space character
    split_string = string.split()
    # return the list of strings
    return split_string