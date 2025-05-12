"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""
def text_starta_endb(text):
    """
    :param text: string
    :return: bool
    """
    if text.startswith('a') and text.endswith('b'):
        return True
    else:
        return False

# Test
assert text_starta_endb("aabbbb")
assert text_starta_endb("ab")
assert text_starta_endb("acb")
assert text_starta_endb("abcd")
assert text_starta_endb("a")
assert text_starta_endb("abab")
assert text_starta_endb("abbbbb")
assert text_starta_endb("abccc")
assert text_starta_endb("abbbbab")
assert text_starta_endb("abbbba")
assert text_starta_endb("abbbbbb")
assert text_starta_endb("abbbbbbb")
assert text_starta_endb("abbbbbbbb")
assert text_starta_endb("abbbbbbbbb")
assert text_starta_endb("abbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
assert text_starta_endb("abbbbbbbbbbbbbbbbb