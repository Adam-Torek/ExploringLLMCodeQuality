def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome.
    postfix = ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            postfix = string[:i]
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return string + postfix[::-1]


def make_palindrome_recursive(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome_recursive('')
    ''
    >>> make_palindrome_recursive('cat')
    'catac'
    >>> make_palindrome_recursive('cata')
    'catac'
    """
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome.
    postfix = ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            postfix = string[:i]
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return string + postfix[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
</s>