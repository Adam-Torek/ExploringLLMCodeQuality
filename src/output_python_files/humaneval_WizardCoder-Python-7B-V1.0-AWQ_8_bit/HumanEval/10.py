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
    assert make_palindrome('abcdefghij') == 'abcdefghijijfedcba'
    assert make_palindrome('abcdefghijkl') == 'abcdefghijkljfedcba'
    assert make_palindrome('abcdefghijklm') == 'abcdefghijklmmlkjihgfedcba'
    assert make_palindrome('abcdefghijklmn') == 'abcdefghijklmnijklhgfedcba'
    assert make_palindrome('abcdefghijklmnop') == 'abcdefghijklmnopmnoijklhgfedcba'
    assert make_palindrome('abcdefghijklmnopq') == 'abcdefghijklmnopqpqojklhgfedcba'
    assert make_palindrome('abcdefghijklmnopqr') == 'abcdefghijklmnopqrqorpqojlhgfedcba'
    assert make_palindrome('abcdefghijklmnopqrs') == 'abcdefghijklmnopqrststqrpsqojlhgfedcba'
    assert make_palindrome('abcdefghijklmnopqrstu') == 'abcdefghijklmnopqrstuvutsuqrpsqojlhgfedcba'
    assert make_palindrome('abcdefghijklmnopqrstuvw') == 'abcdefghijklmnopqrstuvwtwvutsrqpohgfedcba'
    assert make_palindrome('abcdefghijklmnopqrstuvwx') == 'abcdefghijklmnopqrstuvwxtwvutsxqpohgfedcba'
    assert make_palindrome('abcdefghijklmnopqrstuvwxyz') == 'abcdefghijklmnopqrstuvwxyzzyxwvutsyqpoh