"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""

def list_to_float(list_of_lists):
    """
    >>> list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] )
    [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
    """
    return [(float(x[0]), float(x[1])) for x in list_of_lists]


def list_to_float_2(list_of_lists):
    """
    >>> list_to_float_2( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] )
    [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
    """
    return [(float(x[0]), float(x[1])) for x in list_of_lists if x[0].isdigit() and x[1].isdigit()]


def list_to_float_3(list_of_lists):
    """
    >>> list_to_float_3( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] )
    [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
    """
    return [(float(x[0]), float(x[1])) for x in list_of_lists if x[0].isdigit() and x[1].isdigit()]


def list_to_float_4(list_of_lists):
    """
    >>> list_to_float_4( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] )
    [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
    """
    return [(float(x[0]), float(x[1])) for x in list_of_lists if x[0].isdigit() and x[1].isdigit()]


def list_to_float_5(list_of_lists):
    """
    >>> list_to_float_5( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] )
    [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
    """
    return [(float(x[0]), float(x[1])) for x in list_of_lists if x[0].isdigit() and x[1].isdigit()]


def list_to_float_6(list_of_lists):
    """
    >>> list_to_float_6( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] )
    [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
    """
    return [(float(x[0]), float(x[1])) for x in list_of_lists if x[0].isdigit() and x[1].isdigit()]


def list_to_float_7