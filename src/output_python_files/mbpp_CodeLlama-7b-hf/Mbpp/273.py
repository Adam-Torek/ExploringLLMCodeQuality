"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""


def substract_elements(t1, t2):
    """
    >>> substract_elements((10, 4, 5), (2, 5, 18))
    (8, -1, -13)
    """
    return tuple(a - b for a, b in zip(t1, t2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
</s>