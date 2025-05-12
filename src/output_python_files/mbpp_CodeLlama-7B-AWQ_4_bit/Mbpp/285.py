"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""


def text_match_two_three(text):
    """
    :param text: str
    :return: bool
    """
    if text.count('a') == 0:
        return False
    else:
        return text.count('a') == text.count('b') or text.count('a') == text.count('b') + 1


if __name__ == '__main__':
    print(text_match_two_three("ac"))
    print(text_match_two_three("ab"))
    print(text_match_two_three("abc"))
    print(text_match_two_three("abbb"))
    print(text_match_two_three("abbbb"))
    print(text_match_two_three("abbbbb"))
    print(text_match_two_three("abbbbbb"))
    print(text_match_two_three("abbbbbbb"))
    print(text_match_two_three("abbbbbbbb"))
    print(text_match_two_three("abbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_three("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(text_match_two_