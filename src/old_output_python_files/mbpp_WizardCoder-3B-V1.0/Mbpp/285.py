"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""
def text_match_two_three(text):
    if text.startswith('a') and (text[1:].count('b') >= 2 or text[1:].count('b') == 1):
        return True
    else:
        return False

# Test cases
assert text_match_two_three("ac")==(False)
assert text_match_two_three("ab")==(True)
assert text_match_two_three("abc")==(True)
assert text_match_two_three("abbb")==(True)
assert text_match_two_three("abbbbb")==(False)<|endoftext|>