"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""

def replace_char(string, old_char, new_char):
    """
    This function takes a string and two characters as input and returns a new string with all occurrences of old_char replaced by new_char.
    """
    new_string = string.replace(old_char, new_char)
    return new_string

# Test the function
assert replace_char("polygon",'y','l')==("pollgon")