"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""

def remove_Occ(string, char):
    """
    This function removes the first and last occurrence of a given character from the string.
    :param string: string
    :param char: character
    :return: string
    """
    string = list(string)
    string.remove(char)
    string.remove(char)
    return ''.join(string)


# Test the function
assert remove_Occ("hello","l") == "heo"