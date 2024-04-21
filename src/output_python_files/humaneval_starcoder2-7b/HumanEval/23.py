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
    >>> strncat('abc', 'def', 2)
    'abcdef'
    >>> strncat('abc', 'def', 3)
    'abcdef'
    >>> strncat('abc', 'def', 4)
    'abcdef'
    >>> strncat('abc', 'def', 0)
    'abc'
    >>> strncat('abc', 'def', -1)
    'abc'
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
    >>> strchr('abc', '')
    ''
    """

def strncmp(string1: str, string2: str, n: int) -> int:
    """ Compare two strings, but only n characters
    >>> strncmp('abc', 'def', 2)
    0
    >>> strncmp('abc', 'def', 3)
    0
    >>> strncmp('abc', 'def', 4)
    0
    >>> strncmp('abc', 'def', 0)
    0
    >>> strncmp('abc', 'def', -1)
    0
    >>> strncmp('abc', 'def', 1)
    -1
    >>> strncmp('abc', 'def', 2)
    -1
    >>> strncmp('abc', 'def', 3)
    -1
    >>> strncmp('abc', 'def', 4)
    -1
    >>> strncmp('abc', 'def', 5)
    -1
    >>> strncmp('abc', 'def', 6)
    -1
    >>> strncmp('abc', 'def', 7)
    -1
    >>> strncmp('abc', 'def', 8)
    -1
    >>> strncmp('abc', 'def', 9)
    -1
    >>> strncmp('abc', 'def', 10)
    -1
    >>> strncmp('abc', 'def', 11)
    -1
    >>> strncmp('abc', 'def', 12)
    -1
    >>> strncmp('abc', 'def', 13)
    -1
    >>> strncmp('abc', 'def', 14)
    -1
    >>> strncmp('abc', 'def', 15)
    -1
    >>> strncmp('abc', 'def', 16)
    -1
    >>> strncmp('abc', 'def', 17)
    -1
    >>> strncmp('abc', 'def', 18)
    -1
    >>> strncmp('abc', 'def', 19)
    -1
    >>> strncmp('abc', 'def', 20)
    -1
    >>> strncmp('abc', 'def', 21)
    -1
    >>> strncmp('abc', 'def', 22)
    -1
    >>> strncmp('abc', 'def', 23)
    -1
    >>> strncmp('abc', 'def', 24)
    -1
    >>> strncmp('abc', 'def', 25)
    -1
    >>> strncmp('abc', 'def', 26)
    -1
    >>> strncmp('abc', 'def', 27)
    -1
    >>> strncmp('abc', 'def', 28)
    -1
    >>> strncmp('abc', 'def', 29)
    -1
    >>> strncmp('abc', 'def', 30)
    -1
    >>> strncmp('abc', 'def', 31)
    -1
    >>> strncmp('abc', 'def', 32)
    -1
    >>> strncmp('abc', 'def', 33)
    -1
    >>> str