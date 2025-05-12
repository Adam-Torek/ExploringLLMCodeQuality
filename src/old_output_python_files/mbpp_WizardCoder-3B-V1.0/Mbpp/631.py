"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""

def replace_spaces(string):
    return string.replace(' ', '_')

# Test the function
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'<|endoftext|>