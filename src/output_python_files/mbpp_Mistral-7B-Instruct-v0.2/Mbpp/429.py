"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""
def and_tuples(tuple1, tuple2):
    """
    :param tuple1: first tuple
    :param tuple2: second tuple
    :return: tuple of elementwise and tuples
    """
    elementwise = tuple(map(lambda x, y: x if x == y else None, tuple1, tuple2))
    tuples = list(filter(lambda x: x is not None, [tuple(i) for i in zip(tuple1, tuple2)]))
    return elementwise, tuples

assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)