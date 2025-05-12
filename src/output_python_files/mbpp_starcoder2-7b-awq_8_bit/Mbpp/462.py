"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange','red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green','red'], ['green','red', 'orange'], ['blue'], ['blue', 'orange'], ['blue','red'], ['blue','red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green','red'], ['blue', 'green','red', 'orange']]
"""

def combinations_list(lst):
    """
    :param lst: list of strings
    :return: list of lists of strings
    """
    if len(lst) == 0:
        return [[]]
    else:
        return [lst[0]] + combinations_list(lst[1:])

def combinations_list_2(lst):
    """
    :param lst: list of strings
    :return: list of lists of strings
    """
    if len(lst) == 0:
        return [[]]
    else:
        return [lst[0]] + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst[1:]) + combinations_list_2(lst