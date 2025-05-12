"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""


def text_match_three(text):
    """
    :param text: str
    :return: bool
    """
    return text.startswith('a') and text[1:].startswith('bbb')


if __name__ == '__main__':
    print(text_match_three('abbb'))
    print(text_match_three('a'))
    print(text_match_three('abbbb'))
    print(text_match_three('ac'))
    print(text_match_three('aabb'))
    print(text_match_three('aabbb'))
    print(text_match_three('aabbbb'))
    print(text_match_three('aabbbbb'))
    print(text_match_three('aabbbbbb'))
    print(text_match_three('aabbbbbbb'))
    print(text_match_three('aabbbbbbbb'))
    print(text_match_three('aabbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
    print(text_match_three('aabbbbbbbbb