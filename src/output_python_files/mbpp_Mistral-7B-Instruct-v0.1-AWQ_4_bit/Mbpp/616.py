"""
Write a function which takes two tuples of the same length and performs the element wise modulo.
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
"""

def tuple_modulo(tuple1, tuple2):
    """
    Takes two tuples of the same length and performs the element wise modulo.
    :param tuple1: tuple of integers
    :param tuple2: tuple of integers
    :return: tuple of integers
    """
    assert len(tuple1) == len(tuple2), "Tuples must be of the same length"
    return tuple([x % y for x, y in zip(tuple1, tuple2)])


# Test
tuple1 = (10, 4, 5, 6)
tuple2 = (5, 6, 7, 5)
assert tuple_modulo(tuple1, tuple2) == (0, 4, 5, 1)