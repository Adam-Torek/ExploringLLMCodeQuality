"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""
def text_match_wordz_middle(text):
    """
    :param text: string
    :return: boolean
    """
    words = text.split()
    for word in words:
        if len(word) > 1 and word[0] != 'z' and word[-1] != 'z':
            if 'z' in word[1:-1]:
                return True
    return False

# Test
assert text_match_wordz_middle("pythonzabc.")==True
assert text_match_wordz_middle("applezbanana")==True
assert text_match_wordz_middle("zapplezbanana")==False
assert text_match_wordz_middle("zapplezbanana z")==False
assert text_match_wordz_middle("zapplezbanana zz")==False
assert text_match_wordz_middle("zapplezbanana zz z")==False
assert text_match_wordz_middle("zapplezbanana zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz zz zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz zz zz zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz zz zz zz zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz zz zz zz zz zz zz zz zz zz zz")==False
assert text_match_wordz_middle("zapplezbanana zz zz zz zz zz zz zz zz zz zz zz zz zz zz zz zz zz zz")==False
assert text_match_wordz_