"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""
def subtract_elements(tuple1, tuple2):
    """
    This function takes in two tuples as arguments and returns a new tuple with the difference of the elements at the same index.
    """
    result = ()
    for i in range(len(tuple1)):
        result += (tuple1[i] - tuple2[i],)
    return result

# Test the function
assert subtract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)