"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""
def replace_blank(string, character):
    """
    :param string: string
    :param character: character
    :return: string
    """
    return string.replace(" ", character)


# assert replace_blank("hello people",'@')==("hello@people")
# assert replace_blank("hello people",'1')==("hello1people")