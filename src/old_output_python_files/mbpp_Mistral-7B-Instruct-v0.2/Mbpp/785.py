"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

import re

def tuple_str_int(tuple_str):
    """
    :param tuple_str: string representation of tuple
    :return: tuple of integers
    """
    pattern = r'\(([0-9,]+)\)'
    match = re.search(pattern, tuple_str)
    if match:
        return tuple(map(int, match.group(1).split(',')))
    else:
        raise ValueError("Invalid tuple string")

if __name__ == '__main__':
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3, 4, 5)") == (1, 2, 3, 4, 5)
    assert tuple_str_int("(1, 2)") == (1, 2)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("(1)") == (1,)
    assert tuple_str_int("