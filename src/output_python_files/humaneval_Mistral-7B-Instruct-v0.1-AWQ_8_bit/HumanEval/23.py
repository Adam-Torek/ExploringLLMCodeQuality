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
    >>> strreplace('12345', '23', '123')
    '12345'
    >>> strreplace('12345', '23', '1234')
    '12345'
    """
    return string.replace(old, new)

def strformat(string: str, format: str) -> str:
    """ Return formatted string
    >>> strformat('12345', '{0:03d}')
    '001'
    >>> strformat('12345', '{0:03d}')
    '123'
    """
    return string.format(format)

def strcasecmp(string1: str, string2: str) -> int:
    """ Return -1 if string1 < string2, 0 if string1 == string2, 1 if string1 > string2
    >>> strcasecmp('abc', 'ABC')
    -1
    >>> strcasecmp('abc', 'abc')
    0
    >>> strcasecmp('abc', 'ABC')
    1
    """
    return string1.casecmp(string2)

def stricmp(string1: str, string2: str) -> int:
    """ Return -1 if string1 < string2, 0 if string1 == string2, 1 if string1 > string2
    >>> stricmp('abc', 'ABC')
    -1
    >>> stricmp('abc', 'abc')
    0
    >>> stricmp('abc', 'ABC')
    1
    """
    return string1.icmp(string2)

def strlower(string: str) -> str:
    """ Return lowercase version of given string
    >>> strlower('ABC')
    'abc'
    >>> strlower('abc')
    'abc'
    """
    return string.lower()

def strupper(string: str) -> str:
    """ Return uppercase version of given string
    >>> strupper('abc')
    'ABC'
    >>> strupper('abc')
    'ABC'
    """
    return string.upper()

def strcapitalize(string: str) -> str:
    """ Return capitalized version of given string
    >>> strcapitalize('abc')
    'Abc'
    >>> strcapitalize('abc')
    'Abc'
    """
    return string.capitalize()

def strtitle(string: str) -> str:
    """ Return title case version of given string
    >>> strtitle('abc')
    'Abc'
    >>> strtitle('abc')
    'Abc'
    """
    return string.title()

def strstrip(string: str) -> str:
    """ Return string with leading and trailing whitespace removed
    >>> strstrip('   abc   ')
    'abc'
    >>> strstrip('   abc   ')
    'abc'
    """