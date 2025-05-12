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
    if len(string) == 0:
        return ''
    if is_palindrome(string):
        return string
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if is_palindrome(string[i:j+1]):
                return string[:i] + string[j:][::-1] + string[i:j+1]
    return ''


def test_make_palindrome():
    """ Test make_palindrome function """
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
    assert make_palindrome('hello') == 'olleh'
    assert make_palindrome('world') == 'dlrow'
    assert make_palindrome('madam') == 'madam'
    assert make_palindrome('racecar') == 'racecar'
    assert make_palindrome('a man a plan a canal Panama') == 'a man a plan a canal Panama'
    assert make_palindrome('not a palindrome') == 'not a palindrome'


if __name__ == '__main__':
    test_make_palindrome()