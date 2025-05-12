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
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            return string + string[:i][::-1]
    return string + string[::-1]

def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
    assert make_palindrome('race') == 'racecar'
    assert make_palindrome('hello') == 'helloh'
    assert make_palindrome('world') == 'worldw'
    assert make_palindrome('python') == 'pythonpytho'
    assert make_palindrome('a') == 'aa'
    assert make_palindrome('ab') == 'aba'
    assert make_palindrome('abc') == 'abcba'
    assert make_palindrome('abcd') == 'abcddcba'
    assert make_palindrome('abcde') == 'abcdeedcba'
    assert make_palindrome('abcdef') == 'abcdefedcba'
    assert make_palindrome('abcdefg') == 'abcdefgfedcba'
    assert make_palindrome('abcdefgh') == 'abcdefgfedcbag'
    assert make_palindrome('abcdefghi') == 'abcdefghihgfedcba'
    assert make_palindrome('abcdefghij') == 'abcdefghihgfedcbaij'
    assert make_palindrome('abcdefghijkl') == 'abcdefghihgfedcbaijkl'
    assert make_palindrome('abcdefghijklm') == 'abcdefghihgfedcbaijklm'
    assert make_palindrome('abcdefghijklmn') == 'abcdefghihgfedcbaijklmn'
    assert make_palindrome('abcdefghijklmno') == 'abcdefghihgfedcbaijklmno'
    assert make_palindrome('abcdefghijklmnop') == 'abcdefghihgfedcbaijklmnopp'
    assert make_palindrome('abcdefghijklmnopq') == 'abcdefghihgfedcbaijklmnoqp'
    assert make_palindrome('abcdefghijklmnopqr') == 'abcdefghihgfedcbaijklmnorpq'
    assert make_palindrome('abcdefghijklmnopqrs') == 'abcdefghihgfedcbaijklmnorpqrs'
    assert make_palindrome('abcdefghijklmnopqrst') == 'abcdefghihgfedcbaijklmnorpqrst'
    assert make_palindrome('abcdefghijklmnopqrstu') == 'abcdefghihgfedcbaijklmnorpqrstu'
    assert make_palindrome('abcdefghijklmnopqrstuv') == 'abcdefghihgfedcbaijklmnorpqrstuv'
    assert make_palindrome('abcdefghijklmnopqrstuvw') == 'abcdefghihgfedcbaijklmnorpqrstuvw'