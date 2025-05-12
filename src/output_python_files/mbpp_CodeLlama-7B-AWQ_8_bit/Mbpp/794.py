"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""


def text_starta_endb(text):
    """
    :param text: str
    :return: bool
    """
    return text.startswith('a') and text.endswith('b')


if __name__ == '__main__':
    print("Example:")
    print(text_starta_endb("aabbbb"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert text_starta_endb("aabbbb")
    assert not text_starta_endb("aabbb")
    assert not text_starta_endb("abbbb")
    assert not text_starta_endb("aaabbb")
    assert not text_starta_endb("aabbb")
    assert not text_starta_endb("aabb")
    assert not text_starta_endb("a")
    assert not text_starta_endb("ab")
    assert not text_starta_endb("ba")
    assert not text_starta_endb("b")
    assert not text_starta_endb("")
    assert not text_starta_endb("bab")
    assert not text_starta_endb("babab")
    assert not text_starta_endb("bababab")
    assert not text_starta_endb("babababab")
    assert not text_starta_endb("bababababab")
    assert not text_starta_endb("babababababab")
    assert not text_starta_endb("bababababababab")
    assert not text_starta_endb("babababababababab")
    assert not text_starta_endb("bababababababababb")
    assert not text_starta_endb("bababababababababab")
    assert not text_starta_endb("babababababababababb")
    assert not text_starta_endb("babababababababababab")
    assert not text_starta_endb("bababababababababababb")
    assert not text_starta_endb("bababababababababababab")
    assert not text_starta_endb("babababababababababababb")
    assert not text_starta_endb("babababababababababababab")
    assert not text_starta_endb("bababababababababababababb")
    assert not text_starta_endb("bababababababababababababab")
    assert not text_starta_endb("babababababababababababababb")
    assert not text_starta_endb("babababababababababababababab")
    assert not text_starta_endb("bababababababababababababababb")
    assert not text_starta_endb("bababababababababababababababab")
    assert not text_starta_endb("babababababababababababababababb")
    assert not text_starta_endb("babababababababababababababababab")
    assert not text_starta_endb("bababababababababababababababababb")
    assert not text_starta_endb("bababababababababababababababababab")
    assert not text_starta_endb("babababababababababababababababababb")
    assert not text_starta_endb("babababababababababababababababababab")
    assert not text_starta_endb("bababababab