"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

def replace_spaces(string):
    """
    This function takes a string as an input and returns the string with all spaces replaced with '%20'
    """
    return string.replace(" ", "%20")

# Test the function
print(replace_spaces("My Name is Dawood"))