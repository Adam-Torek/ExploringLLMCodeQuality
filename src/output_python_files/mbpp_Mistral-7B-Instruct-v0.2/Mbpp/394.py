"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""
def check_distinct(tuple_):
    """
    :param tuple_: tuple to check for duplicates
    :return: boolean value indicating if tuple contains duplicates
    """
    return len(tuple_) != len(set(tuple_))

assert check_distinct((1, 4, 5, 6, 1, 4)) == False
assert check_distinct((1, 4, 5, 6, 1, 4, 7)) == False
assert check_distinct((1, 4, 5, 6, 1, 4, 7, 8)) == True