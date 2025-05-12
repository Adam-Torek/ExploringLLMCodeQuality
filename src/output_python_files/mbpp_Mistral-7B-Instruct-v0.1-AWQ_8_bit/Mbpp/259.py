"""
Write a function to maximize the given two tuples.
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""

def maximize_elements(tuple1, tuple2):
    """
    This function takes two tuples as input and returns the tuple with the maximum elements.
    """
    tuple1_max = max(tuple1, key=lambda x: x[1])
    tuple2_max = max(tuple2, key=lambda x: x[1])
    tuple1_max_index = tuple1.index(tuple1_max)
    tuple2_max_index = tuple2.index(tuple2_max)
    tuple1_max_index_tuple = tuple1[tuple1_max_index]
    tuple2_max_index_tuple = tuple2[tuple2_max_index]
    tuple1_max_tuple = tuple1_max_index_tuple[0], tuple1_max_index_tuple[1]
    tuple2_max_tuple = tuple2_max_index_tuple[0], tuple2_max_index_tuple[1]
    return tuple1_max_tuple, tuple2_max_tuple


# Test the function
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))