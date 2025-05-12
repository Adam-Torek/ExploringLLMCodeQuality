from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


def reverse_string(string: str) -> str:
    """ Reverse a given string
    >>> reverse_string('')
    ''
    >>> reverse_string('hello')
    'olleh'
    """
    return string[::-1]


def is_palindrome(string: str) -> bool:
    """ Check if a given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('hello')
    False
    """
    return string == reverse_string(string)


def main():
    """ Testing the functions
    """
    print(concatenate([]))
    print(concatenate(['a', 'b', 'c']))
    print(reverse_string(''))
    print(reverse_string('hello'))
    print(is_palindrome(''))
    print(is_palindrome('a'))
    print(is_palindrome('racecar'))
    print(is_palindrome('hello'))


if __name__ == '__main__':
    main()