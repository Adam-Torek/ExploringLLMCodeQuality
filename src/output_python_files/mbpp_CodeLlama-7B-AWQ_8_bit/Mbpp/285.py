"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""


def text_match_two_three(text):
    """
    :param text: str
    :return: bool
    """
    return text.count('a') == 1 and text.count('b') in [2, 3]


if __name__ == '__main__':
    print("Example:")
    print(text_match_two_three("ac"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert text_match_two_three("ac") == (False)
    assert text_match_two_three("aac") == (True)
    assert text_match_two_three("aab") == (True)
    assert text_match_two_three("aabb") == (True)
    assert text_match_two_three("aabbb") == (True)
    assert text_match_two_three("aabbbb") == (True)
    assert text_match_two_three("aabbbbb") == (False)
    assert text_match_two_three("aabbbbbb") == (False)
    assert text_match_two_three("aabbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == (False)
    assert text_match_two_three("aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")