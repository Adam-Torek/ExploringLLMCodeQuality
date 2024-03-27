"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""
def text_match_two_three(text):
    if 'a' in text and text.count('b') >= 2:
        return True
    else:
        return False

# Test cases
assert text_match_two_three("ac") == False
assert text_match_two_three("abbb") == True
assert text_match_two_three("abbba") == True
assert text_match_two_three("ab") == False
assert text_match_two_three("aaabbb") == True</s>