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


def strlen_recursive_tail_recursive(string: str) -> int:
    """ Return length of given string
    >>> strlen_recursive_tail_recursive('')
    0
    >>> strlen_recursive_tail_recursive('abc')
    3
    """
    def strlen_recursive_tail_recursive_helper(string: str, length: int) -> int:
        if string == '':
            return length
        else:
            return strlen_recursive_tail_recursive_helper(string[1:], length + 1)
    return strlen_recursive_tail_recursive_helper(string, 0)


def strlen_recursive_tail_recursive_optimized(string: str) -> int:
    """ Return length of given string
    >>> strlen_recursive_tail_recursive_optimized('')
    0
    >>> strlen_recursive_tail_recursive_optimized('abc')
    3
    """
    def strlen_recursive_tail_recursive_optimized_helper(string: str, length: int) -> int:
        if string == '':
            return length
        else:
            return strlen_recursive_tail_recursive_optimized_helper(string[1:], length + 1)
    return strlen_recursive_tail_recursive_optimized_helper(string, 0)


def strlen_recursive_tail_recursive_optimized_2(string: str) -> int:
    """ Return length of given string
    >>> strlen_recursive_tail_recursive_optimized_2('')
    0
    >>> strlen_recursive_tail_recursive_optimized_2('abc')
    3
    """
    def strlen_recursive_tail_recursive_optimized_2_helper(string: str, length: int) -> int:
        if string == '':
            return length
        else:
            return strlen_recursive_tail_recursive_optimized_2_helper(string[1:], length + 1)
    return strlen_recursive_tail_recursive_optimized_2_helper(string, 0)


def strlen_recursive_tail_recursive_optimized_3(string: str) -> int:
    """ Return length of given string
    >>> strlen_recursive_tail_recursive_optimized_3('')
    0
    >>> strlen_recursive_tail_recursive_optimized_3('abc')
    3
    """
    def strlen_recursive_tail_recursive_optimized_3_helper(string: str, length: int) -> int:
        if string == '':
            return length
        else:
            return strlen_recursive_tail_recursive_optimized_3_helper(string[1:], length + 1)
    return strlen_recursive_tail_recursive_optimized_3_helper(string, 0)


def strlen_recursive_tail_recursive_optimized_4(string: str) -> int:
    """ Return length of given string
    >>> strlen_recursive_tail_recursive_optimized_4('')
    0
    >>> strlen_recursive_tail_recursive_optimized_4('abc')
    3
    """
    def strlen_recursive_tail_recursive_optimized_4_helper(string: str, length: int) -> int:
        if string == '':
            return length
        else:
            return strlen_recursive_tail_recursive_optimized_4_helper(string[1:], length + 1)
    return strlen