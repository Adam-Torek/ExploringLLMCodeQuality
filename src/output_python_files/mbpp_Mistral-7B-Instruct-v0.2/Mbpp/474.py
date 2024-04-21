"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""
def replace_char(string, char_to_replace, new_char):
    """
    Replace all occurrences of char_to_replace with new_char in string.

    Args:
        string: str, the string to modify.
        char_to_replace: str, the character to replace.
        new_char: str, the character to replace char_to_replace with.

    Returns:
        str, the modified string.
    """
    return string.replace(char_to_replace, new_char)

assert replace_char("polygon",'y','l')==("pollgon")
assert replace_char("hello",'l','o')==("heooo")
assert replace_char("python",'t','h')==("pyhthon")</s>