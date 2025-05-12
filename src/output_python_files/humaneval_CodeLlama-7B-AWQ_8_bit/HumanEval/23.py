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


def strlen_iterative_2(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_2('')
    0
    >>> strlen_iterative_2('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length


def strlen_iterative_3(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_3('')
    0
    >>> strlen_iterative_3('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length


def strlen_iterative_4(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_4('')
    0
    >>> strlen_iterative_4('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length


def strlen_iterative_5(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_5('')
    0
    >>> strlen_iterative_5('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length


def strlen_iterative_6(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_6('')
    0
    >>> strlen_iterative_6('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length


def strlen_iterative_7(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_7('')
    0
    >>> strlen_iterative_7('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length


def strlen_iterative_8(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_8('')
    0
    >>> strlen_iterative_8('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length


def strlen_iterative_9(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_9('')
    0
    >>> strlen_iterative_9('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length


def strlen_iterative_10(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_10('')
    0
    >>> strlen_iterative_10('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length


def strlen_iterative_11(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_11('')
    0