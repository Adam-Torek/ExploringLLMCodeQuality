"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""

def recursive_list_sum(lst):
    """
    Recursively sums all the elements in a list.
    :param lst: list
    :return: sum of all elements in the list
    """
    if isinstance(lst, list):
        return sum(recursive_list_sum(sublist) for subset in lst)
    else:
        return lst


assert recursive_list_sum(([1, 2, [3,4],[5,6]]) == 21)