"""
Write a function to maximize the given two tuples.
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""

def maximize_elements(tuple1, tuple2):
    """
    This function takes two tuples as input and returns the tuple with the maximum elements.
    """
    max_tuple = tuple1
    for element in tuple2:
        if element[0] > max_tuple[0]:
            max_tuple = element
        elif element[1] > max_tuple[1]:
            max_tuple = element
    return max_tuple

assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))