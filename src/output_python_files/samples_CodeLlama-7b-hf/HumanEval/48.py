def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text == text[::-1]


def is_palindrome_recursive(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_recursive('')
    True
    >>> is_palindrome_recursive('aba')
    True
    >>> is_palindrome_recursive('aaaaa')
    True
    >>> is_palindrome_recursive('zbcd')
    False
    """
    if len(text) <= 1:
        return True
    else:
        return text[0] == text[-1] and is_palindrome_recursive(text[1:-1])


def is_palindrome_recursive_2(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_recursive_2('')
    True
    >>> is_palindrome_recursive_2('aba')
    True
    >>> is_palindrome_recursive_2('aaaaa')
    True
    >>> is_palindrome_recursive_2('zbcd')
    False
    """
    return is_palindrome_recursive_2_helper(text, 0, len(text) - 1)


def is_palindrome_recursive_2_helper(text: str, start: int, end: int):
    if start >= end:
        return True
    elif text[start] == text[end]:
        return is_palindrome_recursive_2_helper(text, start + 1, end - 1)
    else:
        return False


def is_palindrome_recursive_3(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_recursive_3('')
    True
    >>> is_palindrome_recursive_3('aba')
    True
    >>> is_palindrome_recursive_3('aaaaa')
    True
    >>> is_palindrome_recursive_3('zbcd')
    False
    """
    return is_palindrome_recursive_3_helper(text, 0, len(text) - 1)


def is_palindrome_recursive_3_helper(text: str, start: int, end: int):
    if start >= end:
        return True
    elif text[start] == text[end]:
        return is_palindrome_recursive_3_helper(text, start + 1, end - 1)
    else:
        return False


def is_palindrome_recursive_4(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_recursive_4('')
    True
    >>> is_palindrome_recursive_4('aba')
    True
    >>> is_palindrome_recursive_4('aaaaa')
    True
    >>> is_palindrome_recursive_4('zbcd')
    False
    """
    return is_palindrome_recursive_4_helper(text, 0, len(text) - 1)


def is_palindrome_recursive_4_helper(text: str, start: int, end: int):
    if start >= end:
        return True
    elif text[start] == text[end]:
        return is_palindrome_recursive_4_helper(text, start + 1, end - 1)
    else:
        return False


def is_palindrome_recursive_5(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_recursive_5('')
    True
    >>> is_palindrome_recursive_5('aba')
    True
    >>>