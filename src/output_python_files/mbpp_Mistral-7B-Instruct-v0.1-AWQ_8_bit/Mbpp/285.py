"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""

def text_match_two_three(text):
    if 'ab' in text or 'abc' in text:
        return True
    else:
        return False