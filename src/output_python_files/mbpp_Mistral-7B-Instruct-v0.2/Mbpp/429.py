"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""
def and_tuples(tuple1, tuple2):
    """
    :param tuple1: first tuple
    :param tuple2: second tuple
    :return: tuple with elementwise and tuples
    """
    elementwise = tuple(map(lambda x, y: x if x == y else None, tuple1, tuple2))
    tuples = list(zip(tuple1, tuple2))
    tuples = list(filter(lambda x: x[0] != x[1], tuples))
    return elementwise, tuples

assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
assert and_tuples((1, 1, 1, 1), (1, 1, 1, 1)) == (4, [])
assert and_tuples((1, 1, 1, 1), (2, 2, 2, 2)) == (0, [(1, 2), (1, 2), (1, 2), (1, 2)])
assert and_tuples((1, 1, 1, 1), (2, 3, 3, 3)) == (0, [(1, 3), (1, 3), (1, 3), (1, 3)])