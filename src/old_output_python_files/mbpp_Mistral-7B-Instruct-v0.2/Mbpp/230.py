"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""
def replace_blank(string, character):
    """
    Replaces all blank spaces in a given string with a given character
    :param string: str
    :param character: str
    :return: str
    """
    return string.replace(" ", character)

# Testing the function
assert replace_blank("hello people", '@') == "hello@people"
assert replace_blank("hello world", '#') == "hello#world"
assert replace_blank("", '!') == ""
assert replace_blank("hello", '&') == "hello"