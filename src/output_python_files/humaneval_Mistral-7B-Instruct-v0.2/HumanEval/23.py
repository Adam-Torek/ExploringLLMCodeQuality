def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

def strrev(string: str) -> str:
    """ Return reversed string
    >>> strrev('')
    ''
    >>> strrev('abc')
    'cba'
    """
    return string[::-1]

def strcat(string1: str, string2: str) -> str:
    """ Return concatenated string
    >>> strcat('', 'abc')
    'abc'
    >>> strcat('abc', '')
    'abc'
    >>> strcat('abc', 'def')
    'abcdef'
    """
    return string1 + string2

def strcmp(string1: str, string2: str) -> int:
    """ Return 0 if strings are equal, 1 otherwise
    >>> strcmp('', '')
    0
    >>> strcmp('abc', 'abc')
    0
    >>> strcmp('abc', 'def')
    1
    """
    return 1 if string1 != string2 else 0

def strchr(string: str, char: str) -> int:
    """ Return index of first occurrence of char in string, or -1 if not found
    >>> strchr('', 'a')
    -1
    >>> strchr('abc', 'a')
    0
    >>> strchr('abc', 'b')
    1
    """
    return string.find(char)

def strfind(string: str, substring: str) -> int:
    """ Return index of first occurrence of substring in string, or -1 if not found
    >>> strfind('', 'abc')
    -1
    >>> strfind('abc', '')
    0
    >>> strfind('abc', 'abc')
    0
    >>> strfind('abc', 'def')
    -1
    """
    return string.find(substring)

def strrfind(string: str, substring: str) -> int:
    """ Return index of last occurrence of substring in string, or -1 if not found
    >>> strrfind('', 'abc')
    -1
    >>> strrfind('abc', '')
    0
    >>> strrfind('abc', 'a')
    0
    >>> strrfind('abc', 'b')
    1
    >>> strrfind('abcabc', 'abc')
    3
    """
    start = len(string) - len(substring)
    while start >= 0:
        if string[start:start + len(substring)] == substring:
            return start
        start -= 1
    return -1

def strindex(string: str, substring: str) -> int:
    """ Return index of first occurrence of substring in string, or -1 if not found
    >>> strindex('', 'abc')
    -1
    >>> strindex('abc', '')
    0
    >>> strindex('abc', 'abc')
    0
    >>> strindex('abc', 'def')
    -1
    """
    return string.find(substring)

def strrindex(string: str, substring: str) -> int:
    """ Return index of last occurrence of substring in string, or -1 if not found
    >>> strrindex('', 'abc')
    -1
    >>> strrindex('abc', '')
    0
    >>> strrindex('abc', 'a')
    0
    >>> strrindex('abc', 'b')
    1
    >>> strrindex('abcabc', 'abc')
    3
    """
    start = len(string) - len(substring)
    while start