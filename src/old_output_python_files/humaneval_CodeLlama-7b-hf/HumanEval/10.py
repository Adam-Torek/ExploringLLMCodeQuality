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
    if is_palindrome(string):
        return string
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            return string + string[:i-1][::-1]
    return string + string[::-1]


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
    if is_palindrome(string):
        return string
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            return string + string[:i-1][::-1]
    return string + string[::-1]


def make_palindrome_recursive_memo(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome_recursive_memo('')
    ''
    >>> make_palindrome_recursive_memo('cat')
    'catac'
    >>> make_palindrome_recursive_memo('cata')
    'catac'
    """
    if not string:
        return ''
    if is_palindrome(string):
        return string
    if string in memo:
        return memo[string]
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            memo[string] = string + string[:i-1][::-1]
            return memo[string]
    memo[string] = string + string[::-1]
    return memo[string]


def make_palindrome_recursive_memo_2(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome_recursive_memo_2('')
    ''
    >>> make_palindrome_recursive_memo_2('cat')
    'catac'
    >>> make_palindrome_recursive_memo_2('cata')
    'catac'
    """
    if not string:
        return ''
    if is_palindrome(string):
        return string
    if string in memo:
        return memo[string]
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            memo[string