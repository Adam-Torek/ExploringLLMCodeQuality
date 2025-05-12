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

def strsplit(string: str, delimiter: str) -> list:
    """ Return list of substrings by splitting given string with delimiter
    >>> strsplit('12345', '23')
    ['1', '45']
    >>> strsplit('12345', '123')
    ['45']
    """
    return string.split(delimiter)

def strjoin(strings: list, delimiter: str) -> str:
    """ Return joined string with given delimiter
    >>> strjoin(['1', '45'], '23')
    '12345'
    >>> strjoin(['1', '45'], '123')
    '45'
    """
    return ''.join(strings)

def strreplace(string: str, old: str, new: str) -> str:
    """ Return new string with given old string replaced by new string
    >>> strreplace('123abc', '123', '123xyz')
    '123xyz'
    >>> strreplace('123abc', '123', '123xyz')
    '123xyz'
    """
    return string.replace(old, new)

def strlower(string: str) -> str:
    """ Return lowercase string
    >>> strlower('ABC')
    'abc'
    >>> strlower('abc')
    'abc'
    """
    return string.lower()

def strupper(string: str) -> str:
    """ Return uppercase string
    >>> strupper('abc')
    'ABC'
    >>> strupper('abc')
    'ABC'
    """
    return string.upper()

def strcapitalize(string: str) -> str:
    """ Return capitalized string
    >>> strcapitalize('abc')
    'Abc'
    >>> strcapitalize('abc')
    'Abc'
    """
    return string.capitalize()

def strstrip(string: str) -> str:
    """ Return string without leading or trailing white spaces
    >>> strstrip('   abc   ')
    'abc'
    >>> strstrip('   abc   ')
    'abc'
    """
    return string.strip()

def strcenter(string: str, length: int) -> str:
    """ Return centered string
    >>> strcenter('abc', 5)
    '   abc   '
    >>> strcenter('abc', 5)
    '   abc   '
    """
    return string.center(length)

def strljust(string: str, length: int) -> str:
    """ Return left-justified string
    >>> strljust('abc', 5)
    'abc  '
    >>> strljust('abc', 5)
    'abc  '
    """
    return string.ljust(length)

def strrjust(string: str, length: int) -> str:
    """ Return right-justified string
    >>> strrjust('abc', 5)
    '  abc  '
    >>> strrjust('abc', 5)
    '  abc  '
    """
    return string.rjust(length)

def strpad(string: str, length: int, pad