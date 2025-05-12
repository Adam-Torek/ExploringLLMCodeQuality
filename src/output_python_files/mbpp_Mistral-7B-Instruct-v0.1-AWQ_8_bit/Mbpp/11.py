"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""

def remove_Occ(string, char):
    """
    Function to remove first and last occurrence of a given character from the string.
    """
    string = string.replace(char, '', 1)
    string = string.replace(char, '', 1)
    return string

# Testing code
string = "hello"
char = "l"
assert remove_Occ(string, char) == "heo"