def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    i = 0
    while i < len(string):
        i = string.find(substring, i)
        if i == -1:
            break
        count += 1
        i += len(substring)
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()