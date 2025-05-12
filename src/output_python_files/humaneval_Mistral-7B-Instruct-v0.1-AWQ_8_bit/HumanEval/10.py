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
    if string == '':
        return ''
    if is_palindrome(string):
        return string
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if is_palindrome(string[i:j+1]):
                return string[i:j+1] + string[:i][::-1]
    return ''


def test_make_palindrome():
    """ Test make_palindrome function """
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
    assert make_palindrome('cater') == 'caterac'
    assert make_palindrome('catera') == 'caterac'
    assert make_palindrome('caterer') == 'caterac'
    assert make_palindrome('catererer') == 'caterac'
    assert make_palindrome('caterererer') == 'caterac'
    assert make_palindrome('catererererer') == 'caterac'
    assert make_palindrome('caterererererer') == 'caterac'
    assert make_palindrome('catererererererer') == 'caterac'
    assert make_palindrome('caterererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'caterac'
    assert make_palindrome('catererererererererer') == 'cater