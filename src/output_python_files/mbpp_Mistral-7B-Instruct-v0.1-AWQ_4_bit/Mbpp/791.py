"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""

def remove_nested(tuple_list):
    """
    This function removes nested tuples from the given tuple.
    """
    new_tuple = []
    for item in tuple_list:
        if isinstance(item, tuple):
            new_tuple.extend(remove_nested(item))
        else:
            new_tuple.append(item)
    return tuple(new_tuple)


assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)