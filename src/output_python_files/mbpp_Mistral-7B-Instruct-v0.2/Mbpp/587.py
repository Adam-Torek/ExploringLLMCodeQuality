"""
Write a function to convert a list to a tuple.
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
"""
def list_tuple(input_list):
    """
    Converts a given list to a tuple.

    :param input_list: A list to be converted to a tuple.
    :return: A tuple with the same elements as the input list.
    """
    return tuple(input_list)

assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)