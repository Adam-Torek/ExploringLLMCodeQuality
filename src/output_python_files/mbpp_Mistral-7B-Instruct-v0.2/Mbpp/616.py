"""
Write a function which takes two tuples of the same length and performs the element wise modulo.
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
"""
def tuple_modulo(tuple1, tuple2):
    """
    :param tuple1: A tuple of same length as tuple2
    :param tuple2: A tuple of same length as tuple1
    :return: A tuple of same length as tuple1 and tuple2 with the element wise modulo
    """
    return tuple(i % j for i, j in zip(tuple1, tuple2))

assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)</s>