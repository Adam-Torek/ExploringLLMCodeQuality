"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""
def division_elements(tuple1, tuple2):
    """
    This function takes in two tuples as arguments and performs mathematical division element-wise across the given tuples.
    :param tuple1: A tuple of numbers
    :param tuple2: A tuple of numbers
    :return: A tuple of the results of the division operation for each corresponding element in the tuples
    """
    result = ()
    for i in range(len(tuple1)):
        result += (tuple1[i] / tuple2[i],)
    return result

# Test the function
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)