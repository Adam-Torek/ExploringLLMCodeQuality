"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""

def text_match_three(text):
    if "abab" in text:
        return True
    else:
        return False