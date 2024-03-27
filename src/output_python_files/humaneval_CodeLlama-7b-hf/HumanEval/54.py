def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return sorted(s0) == sorted(s1)


def same_chars_v2(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_v2('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_v2('abcd', 'dddddddabc')
    True
    >>> same_chars_v2('dddddddabc', 'abcd')
    True
    >>> same_chars_v2('eabcd', 'dddddddabc')
    False
    >>> same_chars_v2('abcd', 'dddddddabce')
    False
    >>> same_chars_v2('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return sorted(s0) == sorted(s1)


def same_chars_v3(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_v3('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_v3('abcd', 'dddddddabc')
    True
    >>> same_chars_v3('dddddddabc', 'abcd')
    True
    >>> same_chars_v3('eabcd', 'dddddddabc')
    False
    >>> same_chars_v3('abcd', 'dddddddabce')
    False
    >>> same_chars_v3('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return sorted(s0) == sorted(s1)


def same_chars_v4(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_v4('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_v4('abcd', 'dddddddabc')
    True
    >>> same_chars_v4('dddddddabc', 'abcd')
    True
    >>> same_chars_v4('eabcd', 'dddddddabc')
    False
    >>> same_chars_v4('abcd', 'dddddddabce')
    False
    >>> same_chars_v4('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return sorted(s0) == sorted(s1)


def same_chars_v5(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_v5('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_v5('abcd', 'dddddddabc')
    True
    >>> same_chars_v5('dddddddabc', 'abcd')
    True
    >>> same_chars_v5('eabcd', 'dddddddabc')
    False
    >>> same_chars_v5('abcd', 'dddddddabce')
    False
    >>> same_chars_v5('eabcdzzzz', 'dddzzzzzzzddddabc')
    False