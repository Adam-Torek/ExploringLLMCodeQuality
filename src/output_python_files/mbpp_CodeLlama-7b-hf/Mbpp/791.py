"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""


def remove_nested(tup):
    """
    >>> remove_nested((1, 5, 7, (4, 6), 10))
    (1, 5, 7, 10)
    >>> remove_nested((1, 5, 7, (4, 6), 10, (1, 2, 3)))
    (1, 5, 7, 10, (1, 2, 3))
    >>> remove_nested((1, 5, 7, (4, 6), 10, (1, 2, 3), (1, 2, 3)))
    (1, 5, 7, 10, (1, 2, 3), (1, 2, 3))
    >>> remove_nested((1, 5, 7, (4, 6), 10, (1, 2, 3), (1, 2, 3), (1, 2, 3)))
    (1, 5, 7, 10, (1, 2, 3), (1, 2, 3), (1, 2, 3))
    """
    if isinstance(tup, tuple):
        return tuple(remove_nested(x) for x in tup if not isinstance(x, tuple))
    else:
        return tup


if __name__ == "__main__":
    import doctest

    doctest.testmod()
</s>