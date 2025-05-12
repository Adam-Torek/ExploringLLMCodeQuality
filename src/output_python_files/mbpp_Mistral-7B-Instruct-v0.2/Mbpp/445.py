"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""
def index_multiplication(tuple1, tuple2):
    """
    This function performs index wise multiplication of tuple elements in the given two tuples.
    :param tuple1: A tuple of integers or tuples
    :param tuple2: A tuple of integers or tuples
    :return: A tuple of tuples where each tuple is the index wise product of the corresponding tuples in tuple1 and tuple2
    """
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples should have the same length")

    result = tuple(map(lambda x, y: x[i] * y[i] for i in range(len(x))) for x, y in zip(tuple1, tuple2))
    return result

assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))