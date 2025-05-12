"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""

def text_match_wordz(text):
    """
    This function checks if a word contains 'z'
    """
    if 'z' in text:
        return True
    else:
        return False