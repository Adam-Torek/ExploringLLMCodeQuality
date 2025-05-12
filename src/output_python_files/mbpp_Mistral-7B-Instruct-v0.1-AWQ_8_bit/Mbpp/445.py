"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""

def index_multiplication(tuple1, tuple2):
    """
    This function performs index wise multiplication of tuple elements in the given two tuples.
    :param tuple1: first tuple
    :param tuple2: second tuple
    :return: tuple with index wise multiplication of tuple elements
    """
    result = []
    for i in range(len(tuple1)):
        result.append(tuple1[i] * tuple2[i])
    return tuple(result)


# assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
print(index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)))