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
    s0 = s0.lower()
    s1 = s1.lower()
    s0 = ''.join(sorted(s0))
    s1 = ''.join(sorted(s1))
    return s0 == s1


def same_chars_in_order(s0: str, s1: str):
    """
    Check if two words have the same characters in the same order.
    >>> same_chars_in_order('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_in_order('abcd', 'dddddddabc')
    True
    >>> same_chars_in_order('dddddddabc', 'abcd')
    True
    >>> same_chars_in_order('eabcd', 'dddddddabc')
    False
    >>> same_chars_in_order('abcd', 'dddddddabce')
    False
    >>> same_chars_in_order('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    s0 = s0.lower()
    s1 = s1.lower()
    s0 = ''.join(sorted(s0))
    s1 = ''.join(sorted(s1))
    return s0 == s1


def same_chars_in_order_with_spaces(s0: str, s1: str):
    """
    Check if two words have the same characters in the same order,
    with spaces included.
    >>> same_chars_in_order_with_spaces('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_in_order_with_spaces('abcd', 'dddddddabc')
    True
    >>> same_chars_in_order_with_spaces('dddddddabc', 'abcd')
    True
    >>> same_chars_in_order_with_spaces('eabcd', 'dddddddabc')
    False
    >>> same_chars_in_order_with_spaces('abcd', 'dddddddabce')
    False
    >>> same_chars_in_order_with_spaces('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    s0 = s0.lower()
    s1 = s1.lower()
    s0 = ''.join(sorted(s0))
    s1 = ''.join(sorted(s1))
    s0 = ''.join(s0.split())
    s1 = ''.join(s1.split())
    return s0 == s1


def same_chars_in_order_with_spaces_and_punctuation(s0: str, s1: str):
    """
    Check if two words have the same characters in the same order,
    with spaces, punctuation, and case included.
    >>> same_chars_in_order_with_spaces_and_punctuation('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_in_order_with_spaces_and_punctuation('abcd', 'dddddddabc')
    True
    >>> same_chars_in_order_with_spaces_and_punctuation('dddddddabc', 'abcd')
    True
    >>> same_chars_in_order_with_spaces_and_punctuation('eab