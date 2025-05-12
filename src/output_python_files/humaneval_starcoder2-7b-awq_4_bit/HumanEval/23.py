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

def strcmp(string1: str, string2: str) -> int:
    """ Compare two strings
    >>> strcmp('abc', 'abc')
    0
    >>> strcmp('abc', 'abd')
    -1
    >>> strcmp('abd', 'abc')
    1
    """

def strcpy(string1: str, string2: str) -> str:
    """ Copy string2 to string1
    >>> strcpy('abc', 'def')
    'def'
    >>> strcpy('abc', '')
    ''
    >>> strcpy('', 'def')
    'def'
    """

def strncat(string1: str, string2: str, n: int) -> str:
    """ Concatenate string2 to string1, but only up to n characters
    >>> strncat('abc', 'def', 2)
    'abcdef'
    >>> strncat('abc', 'def', 3)
    'abcde'
    >>> strncat('abc', 'def', 4)
    'abcde'
    >>> strncat('abc', 'def', 5)
    'abcdef'
    """

def strncmp(string1: str, string2: str, n: int) -> int:
    """ Compare string1 and string2, but only up to n characters
    >>> strncmp('abc', 'abc', 2)
    0
    >>> strncmp('abc', 'abd', 2)
    -1
    >>> strncmp('abd', 'abc', 2)
    1
    """

def strncpy(string1: str, string2: str, n: int) -> str:
    """ Copy string2 to string1, but only up to n characters
    >>> strncpy('abc', 'def', 2)
    'de'
    >>> strncpy('abc', 'def', 3)
    'def'
    >>> strncpy('abc', 'def', 4)
    'def'
    >>> strncpy('abc', 'def', 5)
    'def'
    """

def strstr(string: str, substring: str) -> str:
    """ Return first occurrence of substring in string
    >>> strstr('abc', 'a')
    'a'
    >>> strstr('abc', 'b')
    'b'
    >>> strstr('abc', 'c')
    'c'
    >>> strstr('abc', 'd')
    ''
    """

def strspn(string: str, substring: str) -> int:
    """ Return number of characters in string that are in substring
    >>> strspn('abc', 'a')
    1
    >>> strspn('abc', 'b')
    1
    >>> strspn('abc', 'c')
    1
    >>> strspn('abc', 'd')
    0
    """

def strcspn(string: str, substring: str) -> int:
    """ Return number of characters in string that are not in substring
    >>> strcspn('abc', 'a')
    2
    >>> strcspn('abc', 'b')
    2
    >>> strcspn('abc', 'c')
    2
    >>> strcspn('abc', 'd')
    3
    """

def strpbrk(string: str, substring: str) -> str:
    """ Return first occurrence of any character in substring in string
    >>>