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
assert text_starta_endb("a")
assert text_starta_endb("abcd")
assert text_starta_endb("xyz")
assert text_starta_endb("")
assert text_starta_endb("abbbba")
assert text_starta_endb("aabbbba")
assert text_starta_endb("aabbbbaa")
assert text_starta_endb("aabbbbaaa")
assert text_starta_endb("aabbbbaaaa")
assert text_starta_endb("aabbbbaaaaa")
assert text_starta_endb("aabbbbaaaaaa")
assert text_starta_endb("aabbbbaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbbbaaaaaaaa")
assert text_starta_endb("aabbb