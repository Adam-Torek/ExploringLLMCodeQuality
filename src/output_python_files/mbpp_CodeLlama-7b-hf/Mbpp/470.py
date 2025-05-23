"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""


def add_pairwise(t):
    """
    >>> add_pairwise((1, 5, 7, 8, 10))
    (6, 12, 15, 18)
    >>> add_pairwise((1, 2, 3, 4, 5))
    (3, 5, 7, 9)
    >>> add_pairwise((1, 2, 3))
    (3, 5)
    >>> add_pairwise((1, 2))
    (3)
    >>> add_pairwise((1))
    ()
    >>> add_pairwise(())
    ()
    """
    return tuple(a + b for a, b in zip(t, t[1:]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()