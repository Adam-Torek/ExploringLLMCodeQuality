"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""


def tuple_str_int(tuple_str):
    """
    >>> tuple_str_int("(7, 8, 9)")
    (7, 8, 9)
    """
    return tuple(map(int, tuple_str[1:-1].split(",")))


if __name__ == "__main__":
    import doctest

    doctest.testmod()