"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""
def text_match_wordz(text):
    words = text.split()
    for word in words:
        if 'z' in word:
            return True
    return False

# Test the function
assert text_match_wordz("pythonz.") == True
assert text_match_wordz("the quick brown fox jumps over the lazy dog") == False
assert text_match_wordz("apple zucchini pizza") == True
assert text_match_wordz("racecar zebra") == True