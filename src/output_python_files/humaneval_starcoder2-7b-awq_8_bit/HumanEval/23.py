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
    """ Return first occurence of char in string
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
    >>> strcmp('abc', 'abb')
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
    """ Concatenate string2 to string1, but only n characters
    >>> strncat('abc', 'def', 2)
    'abcdef'
    >>> strncat('abc', 'def', 3)
    'abcde'
    >>> strncat('abc', 'def', 4)
    'abcde'
    >>> strncat('abc', 'def', 5)
    'abcde'
    """

def strncmp(string1: str, string2: str, n: int) -> int:
    """ Compare string1 and string2, but only n characters
    >>> strncmp('abc', 'abc', 2)
    0
    >>> strncmp('abc', 'abc', 3)
    0
    >>> strncmp('abc', 'abc', 4)
    0
    >>> strncmp('abc', 'abc', 5)
    0
    >>> strncmp('abc', 'abd', 2)
    0
    >>> strncmp('abc', 'abd', 3)
    0
    >>> strncmp('abc', 'abd', 4)
    0
    >>> strncmp('abc', 'abd', 5)
    0
    >>> strncmp('abc', 'abb', 2)
    0
    >>> strncmp('abc', 'abb', 3)
    0
    >>> strncmp('abc', 'abb', 4)
    0
    >>> strncmp('abc', 'abb', 5)
    0
    >>> strncmp('abc', 'abd', 2)
    0
    >>> strncmp('abc', 'abd', 3)
    0
    >>> strncmp('abc', 'abd', 4)
    0
    >>> strncmp('abc', 'abd', 5)
    0
    >>> strncmp('abc', 'abd', 2)
    0
    >>> strncmp('abc', 'abd', 3)
    0
    >>> strncmp('abc', 'abd', 4)
    0
    >>> strncmp('abc', 'abd', 5)
    0
    >>> strncmp('abc', 'abd', 2)
    0
    >>> strncmp('abc', 'abd', 3)
    0
    >>> strncmp('abc', 'abd', 4)
    0
    >>> strncmp('abc', 'abd', 5)
    0
    >>> strncmp('abc', 'abd', 2)
    0
    >>> strncmp('abc', 'abd', 3)
    0
    >>> strncmp('abc', 'abd', 4)
    0
    >>> strncmp('abc', 'abd', 5)
    0
    >>> strncmp('abc', 'abd', 2)
    0
    >>> strncmp('abc', 'abd', 3)
    0
    >>> strncmp('abc', 'abd', 4)
    0
    >>> strncmp('abc', 'abd', 5)
    0
    >>> strncmp('abc', 'abd', 2)
    0
    >>> strncmp('abc', 'abd', 3)
    0
    >>> strncmp('abc', 'abd', 4)
    0
    >>> strncmp('abc',