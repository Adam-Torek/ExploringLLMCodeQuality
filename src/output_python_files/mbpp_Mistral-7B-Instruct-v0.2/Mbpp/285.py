"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""
def text_match_two_three(text):
    """
    :param text: string
    :return: boolean
    """
    if len(text) < 2:
        return False
    elif text[0] == 'a' and text[1:].startswith('bb'):
        return True
    else:
        return False

# Test cases
assert text_match_two_three("ac") == False
assert text_match_two_three("abbb") == True
assert text_match_two_three("abbbb") == True
assert text_match_two_three("ab") == False
assert text_match_two_three("abc") == False
assert text_match_two_three("abbbba") == True
assert text_match_two_three("abbbbb") == True
assert text_match_two_three("abbbbbb") == True
assert text_match_two_three("abbbbbbb") == True
assert text_match_two_three("abbbbbbbb") == True
assert text_match_two_three("abbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == True
assert text_match_two_three