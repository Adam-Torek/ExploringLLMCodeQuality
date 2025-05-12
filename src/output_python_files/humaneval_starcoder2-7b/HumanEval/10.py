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
#    print(string)
    if is_palindrome(string):
        return string
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            return string + string[:i][::-1]
    return string + string[::-1]


def main():
    """ Main function """
    print(make_palindrome(''))
    print(make_palindrome('cat'))
    print(make_palindrome('cata'))
    print(make_palindrome('cataa'))
    print(make_palindrome('cataaa'))
    print(make_palindrome('cataaaa'))
    print(make_palindrome('cataaaaa'))
    print(make_palindrome('cataaaaaa'))
    print(make_palindrome('cataaaaaaa'))
    print(make_palindrome('cataaaaaaaa'))
    print(make_palindrome('cataaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
    print(make_palindrome('cataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa