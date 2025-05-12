"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""

def check_distinct(tuple_):
    """
    :type tuple_: Tuple
    :rtype: Bool
    """
    # create a set from tuple
    set_tuple = set(tuple_)
    # check if length of set is equal to length of tuple
    if len(set_tuple) == len(tuple_):
        return True
    else:
        return False

assert check_distinct((1, 4, 5, 6, 1, 4)) == False