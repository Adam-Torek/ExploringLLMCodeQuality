"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""

import re

def text_starta_endb(text):
    """
    Matches a string that has an 'a' followed by anything, ending in 'b'.
    """
    pattern = r"a.*b"
    match = re.search(pattern, text)
    if match:
        return True
    else:
        return False

text_starta_endb("aabbbb") # True
text_starta_endb("a") # False
text_starta_endb("ab") # False
text_starta_endb("abc") # False