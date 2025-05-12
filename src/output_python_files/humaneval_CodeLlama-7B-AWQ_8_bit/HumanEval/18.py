def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    return string.count(substring)


def how_many_times_no_overlap(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_no_overlap('', 'a')
    0
    >>> how_many_times_no_overlap('aaa', 'a')
    1
    >>> how_many_times_no_overlap('aaaa', 'aa')
    1
    """
    return string.count(substring) - string.count(substring + substring)


def how_many_times_no_overlap_2(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_no_overlap_2('', 'a')
    0
    >>> how_many_times_no_overlap_2('aaa', 'a')
    1
    >>> how_many_times_no_overlap_2('aaaa', 'aa')
    1
    """
    return string.count(substring) - string.count(substring + substring)


def how_many_times_no_overlap_3(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_no_overlap_3('', 'a')
    0
    >>> how_many_times_no_overlap_3('aaa', 'a')
    1
    >>> how_many_times_no_overlap_3('aaaa', 'aa')
    1
    """
    return string.count(substring) - string.count(substring + substring)


def how_many_times_no_overlap_4(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_no_overlap_4('', 'a')
    0
    >>> how_many_times_no_overlap_4('aaa', 'a')
    1
    >>> how_many_times_no_overlap_4('aaaa', 'aa')
    1
    """
    return string.count(substring) - string.count(substring + substring)


def how_many_times_no_overlap_5(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_no_overlap_5('', 'a')
    0
    >>> how_many_times_no_overlap_5('aaa', 'a')
    1
    >>> how_many_times_no_overlap_5('aaaa', 'aa')
    1
    """
    return string.count(substring) - string.count(substring + substring)


def how_many_times_no_overlap_6(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_no_overlap_6('', 'a')
    0
    >>> how_many_times_no_overlap_6('aaa', 'a')
    1
    >>> how_many_times_no_overlap_6('aaaa', 'aa')
    1
    """
    return string.count(substring) - string.count(substring + substring)


def how_many_times_no_overlap_7(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not