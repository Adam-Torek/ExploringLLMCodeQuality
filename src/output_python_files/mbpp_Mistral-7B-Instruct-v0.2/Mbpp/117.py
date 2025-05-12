"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""
def list_to_float(lst):
    """
    Converts all possible convertible elements in a list of lists to floats.

    :param lst: list of lists
    :return: list of lists with all convertible elements converted to floats
    """
    return list(map(lambda x: list(map(lambda y: float(y) if type(y) is str else y, x)), lst))

# Test case
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]