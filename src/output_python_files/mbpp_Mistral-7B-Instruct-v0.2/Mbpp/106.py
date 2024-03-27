"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""
def add_lists(lst, tpl):
    """
    Appends the given list to the given tuple.

    :param lst: list to be appended
    :param tpl: tuple to which the list is to be appended
    :return: tuple with the list appended
    """
    return tpl + lst</s>