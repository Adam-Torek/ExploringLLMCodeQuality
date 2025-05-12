"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""
def replace_spaces(string):
    """
    Replace whitespaces with underscores and vice versa
    :param string: string to be modified
    :return: string with underscores instead of whitespaces and vice versa
    """
    return string.replace(" ", "_").replace("_", " ")

assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
assert replace_spaces('Jumanji_The_Jungle') == 'Jumanji The Jungle'