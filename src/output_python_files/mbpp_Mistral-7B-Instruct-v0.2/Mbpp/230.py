"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""
def replace_blank(string, character):
    """
    Replaces all blank spaces in a given string with a given character.

    :param string: The string to be modified.
    :param character: The character to replace blank spaces with.
    :return: The modified string.
    """
    return string.replace(" ", character)

# Test the function
assert replace_blank("hello people", '@') == "hello@people"