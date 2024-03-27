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
    if is_palindrome(string):
        return string

    for i in range(len(string) - 1, -1, -1):
        if is_palindrome(string[i:]):
            prefix = string[:i]
            suffix = string[i:]
            return prefix + suffix + suffix[:1:-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print(make_palindrome(''))
    print(make_palindrome('cat'))
    print(make_palindrome('cata'))
    print(make_palindrome('racecar'))
    print(make_palindrome('hello'))
    print(make_palindrome('abba'))
    print(make_palindrome('A man a plan a canal Panama'))</s>