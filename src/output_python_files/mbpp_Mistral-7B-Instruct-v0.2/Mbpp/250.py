"""
Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
"""
def count_X(tuple_input, element):
    """
    Function that takes in a tuple and an element and returns the count of the element in the tuple.

    :param tuple_input: A tuple of numbers
    :param element: An integer to be counted in the tuple
    :return: An integer representing the count of the element in the tuple
    """
    count = 0
    for num in tuple_input:
        if num == element:
            count += 1
    return count

# Test the function
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 5) == 3
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 10) == 3
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 2) == 3
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 1) == 0