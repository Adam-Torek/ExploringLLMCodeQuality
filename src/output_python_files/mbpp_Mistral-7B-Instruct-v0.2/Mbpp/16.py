"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""
def text_lowercase_underscore(text):
    """
    :param text: string
    :return: boolean
    """
    return bool(re.search(r'\W[a-z]+\_[a-z]+\w', text))

import re</s>