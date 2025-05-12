def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if string == substring:
        return 1 + len(string) - 1
    else:
        count = 0
        while True:
            pos = string.find(substring, count)
            if pos == -1:
                break
            count += 1
        return count


def test_how_many_times():
    """ Test how_many_times function.
    """
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaa') == 1