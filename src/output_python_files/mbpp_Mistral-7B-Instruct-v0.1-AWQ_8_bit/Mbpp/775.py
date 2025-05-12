"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""

def odd_position(lst):
    """
    :param lst: list of integers
    :return: True if every odd index contains odd numbers of the list, False otherwise
    """
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True