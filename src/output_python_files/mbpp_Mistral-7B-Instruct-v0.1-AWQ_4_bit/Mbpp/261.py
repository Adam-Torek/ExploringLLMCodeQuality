"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""

def division_elements(tuple1, tuple2):
    """
    This function performs element-wise division operation on two tuples.
    :param tuple1: first tuple
    :param tuple2: second tuple
    :return: tuple of division results
    """
    result = []
    for i in range(len(tuple1)):
        result.append(tuple1[i] / tuple2[i])
    return tuple(result)

# Test the function
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)