"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""
def add_tuple(lst, tpl):
    """
    Adds the given tuple to the given list.

    :param lst: list
    :param tpl: tuple
    :return: list
    """
    lst.extend(tpl)
    return lst</s>