def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


def strlen_recursive(string: str) -> int:
    """ Return length of given string
    >>> strlen_recursive('')
    0
    >>> strlen_recursive('abc')
    3
    """
    if string == '':
        return 0
    else:
        return 1 + strlen_recursive(string[1:])


def strlen_iterative(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative('')
    0
    >>> strlen_iterative('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length


def strlen_iterative_with_range(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_range('')
    0
    >>> strlen_iterative_with_range('abc')
    3
    """
    length = 0
    for _ in range(len(string)):
        length += 1
    return length


def strlen_iterative_with_enumerate(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_enumerate('')
    0
    >>> strlen_iterative_with_enumerate('abc')
    3
    """
    length = 0
    for _ in enumerate(string):
        length += 1
    return length


def strlen_iterative_with_zip(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_zip('')
    0
    >>> strlen_iterative_with_zip('abc')
    3
    """
    length = 0
    for _ in zip(string, string):
        length += 1
    return length


def strlen_iterative_with_zip_with_range(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_zip_with_range('')
    0
    >>> strlen_iterative_with_zip_with_range('abc')
    3
    """
    length = 0
    for _ in zip(string, range(len(string))):
        length += 1
    return length


def strlen_iterative_with_zip_with_enumerate(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_zip_with_enumerate('')
    0
    >>> strlen_iterative_with_zip_with_enumerate('abc')
    3
    """
    length = 0
    for _ in zip(string, enumerate(string)):
        length += 1
    return length


def strlen_iterative_with_zip_with_enumerate_with_range(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_zip_with_enumerate_with_range('')
    0
    >>> strlen_iterative_with_zip_with_enumerate_with_range('abc')
    3
    """
    length = 0
    for _ in zip(string, enumerate(range(len(string)))):
        length += 1
    return length


def strlen_iterative_with_zip_with_enumerate_with_range_with_range(
    string: str
) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_zip_with_enumerate_with_range_with_range('')
    0
    >>> strlen_iterative_with_zip_with_enumerate_with_range_with_range('abc')
    3
    """
    length = 0
    for _ in zip(string, enumerate(range(len(string)))):
        length += 1
    return length


def strlen_iterative_with_zip_with_enumerate_with_range_with_range_with_range(
    string: str
) -> int: