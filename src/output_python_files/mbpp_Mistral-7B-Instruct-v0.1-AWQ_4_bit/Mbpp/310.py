"""
Write a function to convert a given string to a tuple of characters.
assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
"""

def string_to_tuple(string):
    """
    Converts a string to a tuple of characters
    """
    return tuple(string.split())

# assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
print(string_to_tuple("python 3.0"))