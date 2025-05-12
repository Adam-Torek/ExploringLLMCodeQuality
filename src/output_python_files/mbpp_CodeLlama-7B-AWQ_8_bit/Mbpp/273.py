"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""


def substract_elements(tuple1, tuple2):
    """
    >>> substract_elements((10, 4, 5), (2, 5, 18))
    (8, -1, -13)
    """
    return tuple(x - y for x, y in zip(tuple1, tuple2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()