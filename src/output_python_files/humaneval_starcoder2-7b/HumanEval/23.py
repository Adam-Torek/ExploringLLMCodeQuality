def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

def strcat(string1: str, string2: str) -> str:
    """ Concatenate two strings
    >>> strcat('abc', 'def')
    'abcdef'
    >>> strcat('abc', '')
    'abc'
    >>> strcat('', 'def')
    'def'
    """

def strncat(string1: str, string2: str, n: int) -> str:
    """ Concatenate two strings, but only n characters from string2
    >>> strncat('abc', 'def', 0)
    'abc'
    >>> strncat('abc', 'def', 1)
    'abcdef'
    >>> strncat('abc', 'def', 2)
    'abcdef'
    >>> strncat('abc', 'def', 3)
    'abcdef'
    >>> strncat('abc', 'def', 4)
    'abcdef'
    >>> strncat('abc', 'def', 5)
    'abcdef'
    >>> strncat('abc', 'def', 6)
    'abcdef'
    """

def strchr(string: str, char: str) -> str:
    """ Return first occurrence of char in string
    >>> strchr('abc', 'a')
    'a'
    >>> strchr('abc', 'b')
    'b'
    >>> strchr('abc', 'c')
    'c'
    >>> strchr('abc', 'd')
    ''
    """

def strncmp(string1: str, string2: str, n: int) -> int:
    """ Compare two strings, but only n characters
    >>> strncmp('abc', 'abc', 0)
    0
    >>> strncmp('abc', 'abc', 1)
    0
    >>> strncmp('abc', 'abc', 2)
    0
    >>> strncmp('abc', 'abc', 3)
    0
    >>> strncmp('abc', 'abc', 4)
    0
    >>> strncmp('abc', 'abc', 5)
    0
    >>> strncmp('abc', 'abc', 6)
    0
    >>> strncmp('abc', 'abc', 7)
    0
    >>> strncmp('abc', 'abc', 8)
    0
    >>> strncmp('abc', 'abc', 9)
    0
    >>> strncmp('abc', 'abc', 10)
    0
    >>> strncmp('abc', 'abc', 11)
    0
    >>> strncmp('abc', 'abc', 12)
    0
    >>> strncmp('abc', 'abc', 13)
    0
    >>> strncmp('abc', 'abc', 14)
    0
    >>> strncmp('abc', 'abc', 15)
    0
    >>> strncmp('abc', 'abc', 16)
    0
    >>> strncmp('abc', 'abc', 17)
    0
    >>> strncmp('abc', 'abc', 18)
    0
    >>> strncmp('abc', 'abc', 19)
    0
    >>> strncmp('abc', 'abc', 20)
    0
    >>> strncmp('abc', 'abc', 21)
    0
    >>> strncmp('abc', 'abc', 22)
    0
    >>> strncmp('abc', 'abc', 23)
    0
    >>> strncmp('abc', 'abc', 24)
    0
    >>> strncmp('abc', 'abc', 25)
    0
    >>> strncmp('abc', 'abc', 26)
    0
    >>> strncmp('abc', 'abc', 27)
    0
    >>> strncmp('abc', 'abc', 28)
    0
    >>> strncmp('abc', 'abc', 29)
    0
    >>> strncmp('abc', 'abc',