"""
Write a function to add a dictionary to the tuple. The output should be a tuple.
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
"""
def add_dict_to_tuple(tuple_input, dict_input):
    """
    Function to add a dictionary to a tuple
    :param tuple_input: tuple
    :param dict_input: dictionary
    :return: tuple
    """
    return tuple_input + (dict_input,)

assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3}) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})