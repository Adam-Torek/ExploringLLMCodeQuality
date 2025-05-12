"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""

def check_distinct(tuple_):
    """
    :param tuple_: tuple
    :return: True if tuple contains no duplicates, False otherwise
    """
    # create a set from tuple
    set_tuple = set(tuple_)
    # check if length of set is equal to length of tuple
    if len(set_tuple) == len(tuple_):
        return True
    else:
        return False