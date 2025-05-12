"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""


def text_match_three(text):
    """
    :param text: str
    :return: bool
    """
    return text.startswith('a') and text[1:].count('b') == 3


if __name__ == '__main__':
    print(text_match_three("abc"))
    print(text_match_three("abbb"))
    print(text_match_three("a"))
    print(text_match_three("ab"))
    print(text_match_three("ac"))
    print(text_match_three("abbbb"))
    print(text_match_three("abbbbb"))
    print(text_match_three("abbbbbb"))
    print(text_match_three("abbbbbbb"))
    print(text_match_three("abbbbbbbb"))
    print(text_match_three("abbbbbbbbb"))
    print(text_match_three("abbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_three("abbbbbbbbbbbbbbbbbbb