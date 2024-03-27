def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

def strcat(string1: str, string2: str) -> str:
    """ Concatenate two strings
    >>> strcat('hello', 'world')
    'helloworld'
    """

def strrev(string: str) -> str:
    """ Reverse a string
    >>> strrev('hello')
    'olleh'
    """

def strsplit(string: str, delimiter: str) -> List[str]:
    """ Split a string into a list of substrings based on a delimiter
    >>> strsplit('hello,world', ',')
    ['hello', 'world']
    """

def strjoin(strings: List[str], delimiter: str) -> str:
    """ Join a list of strings into a single string based on a delimiter
    >>> strjoin(['hello', 'world'], ',')
    'hello,world'
    """

def strcount(string: str, substring: str) -> int:
    """ Count the number of occurrences of a substring in a string
    >>> strcount('hello,world', 'l')
    2
    """

def strreplace(string: str, old_substring: str, new_substring: str) -> str:
    """ Replace all occurrences of a substring with a new substring in a string
    >>> strreplace('hello,world', 'l', 'x')
    'hxe,wrd'
    """

def strstartswith(string: str, prefix: str) -> bool:
    """ Check if a string starts with a given prefix
    >>> strstartswith('hello', 'he')
    True
    >>> strstartswith('hello', 'hi')
    False
    """

def strendswith(string: str, suffix: str) -> bool:
    """ Check if a string ends with a given suffix
    >>> strendswith('hello', 'lo')
    True
    >>> strendswith('hello', 'll')
    False
    """

def strisalpha(string: str) -> bool:
    """ Check if a string contains only alphabetic characters
    >>> strisalpha('hello')
    True
    >>> strisalpha('123')
    False
    """

def strisdigit(string: str) -> bool:
    """ Check if a string contains only digits
    >>> strisdigit('123')
    True
    >>> strisdigit('hello')
    False
    """

def strislower(string: str) -> bool:
    """ Check if a string contains only lowercase characters
    >>> strislower('hello')
    True
    >>> strislower('HELLO')
    False
    """

def strisupper(string: str) -> bool:
    """ Check if a string contains only uppercase characters
    >>> strisupper('HELLO')
    True
    >>> strisupper('hello')
    False
    """

def strisspace(string: str) -> bool:
    """ Check if a string contains only whitespace characters
    >>> strisspace(' ')
    True
    >>> strisspace('')
    True
    >>> strisspace('hello')
    False
    """

def strisalnum(string: str) -> bool:
    """ Check if a string contains only alphanumeric characters
    >>> strisalnum('hello')
    True
    >>> strisalnum('123')
    False
    """

def strisalpha(string: str) -> bool:
    """ Check if a string contains only alphabetic characters
    >>> strisalpha('hello')
    True
    >>> strisalpha('123')
    False
    """

def strislower(string: str) -> bool:
    """ Check if a string contains only lowercase characters
    >>> strislower('hello')
    True
    >>> strislower('HELLO')
    False
    """

def strisupper(string: str) -> bool:
    """ Check if a string contains only uppercase characters
    >>> strisupper('HELLO')
    True
    >>> strisupper('hello')
    False
    """

def strisspace(string: str) -> bool:
    """ Check if a string contains only whitespace characters
    >>> strisspace(' ')
    True
    >>> strisspace('')
    True
    >>> strisspace('hello')
    False
    """

def strisalnum(string: str) -> bool:
    """ Check if a string contains only alphanumeric characters
    >>> strisalnum('hello')
    True
    >>> strisalnum('123')
    False
    """

def strisalpha(string: str) -> bool:
    """ Check if a string contains only alphabetic characters
    >>> strisalpha('hello')
    True
    >>> strisalpha('123')
    False