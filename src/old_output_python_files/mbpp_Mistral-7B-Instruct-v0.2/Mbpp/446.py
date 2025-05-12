"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""
def count_Occurrence(tuple_input, list_input):
    """
    Function to count the occurrence of all elements of list in a tuple.

    :param tuple_input: tuple
    :param list_input: list
    :return: int
    """
    count = {element: 0 for element in list_input}
    for element in tuple_input:
        if element in list_input:
            count[element] += 1
    return sum(count.values())

assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']) == 3
assert count_Occurrence(('a', 'b', 'c', 'd'),['a', 'b']) == 2
assert count_Occurrence(('a', 'b', 'c', 'd'),['c', 'd']) == 2
assert count_Occurrence(('a', 'b', 'c', 'd'),['e']) == 0