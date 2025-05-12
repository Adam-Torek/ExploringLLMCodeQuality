"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""

def substract_elements(tuple1, tuple2):
    """
    Subtracts the elements of the first tuple by the elements of the second tuple with the same index.
    :param tuple1: A tuple of length n
    :param tuple2: A tuple of length n
    :return: A tuple of length n with the subtracted elements
    """
    result = []
    for i in range(len(tuple1)):
        result.append(tuple1[i] - tuple2[i])
    return tuple(result)

# assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
print(substract_elements((10, 4, 5), (2, 5, 18)))