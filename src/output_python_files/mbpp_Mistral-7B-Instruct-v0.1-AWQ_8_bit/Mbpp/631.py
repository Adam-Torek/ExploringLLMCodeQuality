"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""

def replace_spaces(string):
    """
    Function to replace whitespaces with an underscore and vice versa in a given string.
    """
    # Using the replace() method to replace all occurrences of whitespace with an underscore
    # and all occurrences of an underscore with a whitespace
    return string.replace(" ", "_").replace("_", " ")

# Testing the function
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'