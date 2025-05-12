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


def strlen_iterative_with_while(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_while('')
    0
    >>> strlen_iterative_with_while('abc')
    3
    """
    length = 0
    i = 0
    while i < len(string):
        length += 1
        i += 1
    return length


def strlen_iterative_with_for(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_for('')
    0
    >>> strlen_iterative_with_for('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length


def strlen_iterative_with_for_range(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_for_range('')
    0
    >>> strlen_iterative_with_for_range('abc')
    3
    """
    length = 0
    for _ in range(len(string)):
        length += 1
    return length


def strlen_iterative_with_for_range_and_step(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_for_range_and_step('')
    0
    >>> strlen_iterative_with_for_range_and_step('abc')
    3
    """
    length = 0
    for _ in range(0, len(string), 1):
        length += 1
    return length


def strlen_iterative_with_for_range_and_step_and_start(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_for_range_and_step_and_start('')
    0
    >>> strlen_iterative_with_for_range_and_step_and_start('abc')
    3
    """
    length = 0
    for _ in range(1, len(string), 1):
        length += 1
    return length


def strlen_iterative_with_for_range_and_step_and_start_and_end(string: str) -> int:
    """ Return length of given string
    >>> strlen_iterative_with_for_range_and_step_and_start_and_end('')
    0
    >>> strlen_iterative_with_for_range_and_step_and_start_and_end('abc')
    3
    """
    length = 0
    for _ in range(1, len(string), 1):