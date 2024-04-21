"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""
def replace_spaces(string):
    """
    Replace whitespaces with underscores and vice versa in a given string.
    :param string: str
    :return: str
    """
    return string.replace(" ", "_").replace("_", " ")

assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'</s>