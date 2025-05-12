"""
Write a function to find the size in bytes of the given tuple.
assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
"""

import sys


def tuple_size(t):
    """
    >>> tuple_size(("A", 1, "B", 2, "C", 3) )
    48
    """
    return sys.getsizeof(t)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
