def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:
        return 0
    if not string:
        return 0
    if len(substring) > len(string):
        return 0
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count


def how_many_times_no_overlap(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_no_overlap('', 'a')
    0
    >>> how_many_times_no_overlap('aaa', 'a')
    1
    >>> how_many_times_no_overlap('aaaa', 'aa')
    1
    """
    if not substring:
        return 0
    if not string:
        return 0
    if len(substring) > len(string):
        return 0
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            if i + len(substring) == len(string):
                count += 1
            else:
                if string[i + len(substring)] != substring[0]:
                    count += 1
    return count


def how_many_times_no_overlap_2(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_no_overlap_2('', 'a')
    0
    >>> how_many_times_no_overlap_2('aaa', 'a')
    1
    >>> how_many_times_no_overlap_2('aaaa', 'aa')
    1
    """
    if not substring:
        return 0
    if not string:
        return 0
    if len(substring) > len(string):
        return 0
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            if i + len(substring) == len(string):
                count += 1
            else:
                if string[i + len(substring)] != substring[0]:
                    count += 1
    return count


def how_many_times_no_overlap_3(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_no_overlap_3('', 'a')
    0
    >>> how_many_times_no_overlap_3('aaa', 'a')
    1
    >>> how_many_times_no_overlap_3('aaaa', 'aa')
    1
    """
    if not substring:
        return 0
    if not string:
        return 0
    if len(substring) > len(string):
        return 0
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            if i + len(substring) == len(string):
                count += 1
            else:
                if string[i + len(substring)] != substring[0]:
                    count += 1
    return count


def how_many_times_no_overlap_4(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_