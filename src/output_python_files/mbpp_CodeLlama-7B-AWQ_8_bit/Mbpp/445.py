"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""


def index_multiplication(tuple1, tuple2):
    """
    :param tuple1: tuple of tuples
    :param tuple2: tuple of tuples
    :return: tuple of tuples
    """
    assert type(tuple1) == tuple and type(tuple2) == tuple, "Inputs must be tuples"
    assert len(tuple1) == len(tuple2), "Inputs must be of same length"
    assert all(type(i) == tuple for i in tuple1), "Inputs must be tuples"
    assert all(type(i) == tuple for i in tuple2), "Inputs must be tuples"
    assert all(len(i) == 2 for i in tuple1), "Inputs must be tuples of tuples"
    assert all(len(i) == 2 for i in tuple2), "Inputs must be tuples of tuples"
    assert all(type(j) == int for i in tuple1 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(type(j) == int for i in tuple2 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(type(j) == int for i in tuple1 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(type(j) == int for i in tuple2 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(len(i) == 2 for i in tuple1), "Inputs must be tuples of tuples"
    assert all(len(i) == 2 for i in tuple2), "Inputs must be tuples of tuples"
    assert all(len(i) == 2 for i in tuple1), "Inputs must be tuples of tuples"
    assert all(len(i) == 2 for i in tuple2), "Inputs must be tuples of tuples"
    assert all(type(j) == int for i in tuple1 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(type(j) == int for i in tuple2 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(type(j) == int for i in tuple1 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(type(j) == int for i in tuple2 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(len(i) == 2 for i in tuple1), "Inputs must be tuples of tuples"
    assert all(len(i) == 2 for i in tuple2), "Inputs must be tuples of tuples"
    assert all(len(i) == 2 for i in tuple1), "Inputs must be tuples of tuples"
    assert all(len(i) == 2 for i in tuple2), "Inputs must be tuples of tuples"
    assert all(type(j) == int for i in tuple1 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(type(j) == int for i in tuple2 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(type(j) == int for i in tuple1 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(type(j) == int for i in tuple2 for j in i), "Inputs must be tuples of tuples of integers"
    assert all(len(i) == 2 for i in tuple1), "Inputs must be tuples of tuples"
    assert all(len(i) == 2 for i in tuple2), "Inputs must be tuples of tuples"
    assert all(len