def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if len(string) < len(substring):
        return 0
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()