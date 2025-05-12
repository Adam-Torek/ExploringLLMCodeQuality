"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""

def text_lowercase_underscore(text):
    """
    :param text: string
    :return: bool
    """
    for i in range(len(text)):
        if i == 0:
            continue
        if text[i] != '_' and text[i] != text[i-1].lower():
            return False
    return True