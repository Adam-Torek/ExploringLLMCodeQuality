"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""

def list_to_float(lst):
    """
    Converts all possible convertible elements in a list of lists to floats.
    """
    return [(float(x), float(y)) for x, y in lst]

# assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
# assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8"), ("1", "1.0")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0), (1.0, 1.0)]