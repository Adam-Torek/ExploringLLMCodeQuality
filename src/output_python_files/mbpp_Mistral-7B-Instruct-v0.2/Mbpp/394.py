"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""
def check_distinct(tuple_):
    """
    :param tuple_: tuple
    :return: bool
    """
    return len(tuple_) == len(set(tuple_))

assert check_distinct((1, 4, 5, 6, 1, 4)) == False
assert check_distinct((1, 4, 5, 6, 7, 8)) == True</s>