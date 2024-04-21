"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""


def extract_even(t):
    """
    >>> extract_even((4, 5, (7, 6, (2, 4)), 6, 8))
    (4, (6, (2, 4)), 6, 8)
    """
    if isinstance(t, tuple):
        return tuple(extract_even(x) for x in t if isinstance(x, tuple) or x % 2 == 0)
    else:
        return t


if __name__ == "__main__":
    import doctest

    doctest.testmod()
</s>