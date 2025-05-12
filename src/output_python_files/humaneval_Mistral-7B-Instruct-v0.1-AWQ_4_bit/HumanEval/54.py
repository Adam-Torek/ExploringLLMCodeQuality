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
    if len(s0) != len(s1):
        return False
    for i in range(len(s0)):
        if s0[i] != s1[i]:
            return False
    return True


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
    if len(s0) != len(s1):
        return False
    for i in range(len(s0)):
        if s0[i] != s1[i]:
            return False
    return True


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
    if len(s0) != len(s1):
        return False
    for i in range(len(s0)):
        if s0[i] != s1[i]:
            return False
    return True


def same_chars_in_order_with_spaces_and_case(s0: str, s1: str):
    """
    Check if two words have the same characters in the same order,
    with spaces included and case ignored.
    >>> same_chars_in_order_with_spaces_and_case('eAbCdZz', 'dDdZz')
    True
    >>> same_chars_in_order_with_spaces_and_case('abCd', 'dDd')
    True
    >>> same_chars_in_order_with_spaces_and_case('dDd', 'abCd')
    True
    >>> same_chars_in_order_with_spaces_and_case('eAbCdZz', 'dDdZz')
    False
    >>> same_chars_in_order_with_spaces_and_case('abCd', 'dDd')
    False
    >>> same_chars_in_order_with_spaces_and_