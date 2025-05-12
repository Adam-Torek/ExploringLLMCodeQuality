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


def is_palindrome_recursive_memo(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_recursive_memo('')
    True
    >>> is_palindrome_recursive_memo('aba')
    True
    >>> is_palindrome_recursive_memo('aaaaa')
    True
    >>> is_palindrome_recursive_memo('zbcd')
    False
    """
    cache = {}

    def is_palindrome_recursive_memo_helper(text: str):
        if len(text) <= 1:
            return True
        else:
            if text not in cache:
                cache[text] = text[0] == text[-1] and is_palindrome_recursive_memo_helper(text[1:-1])
            return cache[text]

    return is_palindrome_recursive_memo_helper(text)


def is_palindrome_recursive_memo_2(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_recursive_memo_2('')
    True
    >>> is_palindrome_recursive_memo_2('aba')
    True
    >>> is_palindrome_recursive_memo_2('aaaaa')
    True
    >>> is_palindrome_recursive_memo_2('zbcd')
    False
    """
    cache = {}

    def is_palindrome_recursive_memo_helper(text: str):
        if len(text) <= 1:
            return True
        else:
            if text not in cache:
                cache[text] = text[0] == text[-1] and is_palindrome_recursive_memo_helper(text[1:-1])
            return cache[text]

    return is_palindrome_recursive_memo_helper(text)


def is_palindrome_recursive_memo_3(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_recursive_memo_3('')
    True
    >>> is_palindrome_recursive_memo_3('aba')
    True
    >>> is_palindrome_recursive_memo_3('aaaaa')
    True
    >>> is_palindrome_recursive_memo_3('zbcd')
    False
    """
    cache = {}

    def is_palindrome_recursive_memo_helper(text: str):
        if len(text) <= 1:
            return True
        else:
            if text not in cache:
                cache[text] = text[0] == text[-1] and is_palindrome_recursive_memo_helper(text[1:-1])