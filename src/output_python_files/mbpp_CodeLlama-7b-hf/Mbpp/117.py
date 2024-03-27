"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""

def list_to_float(list_of_lists):
    """
    Convert all possible convertible elements in a list of lists to floats.
    :param list_of_lists: list of lists
    :return: list of lists with converted elements
    """
    return [tuple(map(float, i)) for i in list_of_lists]


if __name__ == '__main__':
    print(list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ))
    print(list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0")] ))
    print(list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45")] ))
    print(list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0")] ))
    print(list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0")] ))
    print(list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0")] ))
    print(list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0")] ))
    print(list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0"), ("1", "26.45"), ("7.32", "8"), ("4", "8.0")] ))
    print(list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("