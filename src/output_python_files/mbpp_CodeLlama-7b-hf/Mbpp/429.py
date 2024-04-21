"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""


def and_tuples(t1, t2):
    """
    >>> and_tuples((10, 4, 6, 9), (5, 2, 3, 3))
    (0, 0, 2, 1)
    """
    return tuple(x & y for x, y in zip(t1, t2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
</s>