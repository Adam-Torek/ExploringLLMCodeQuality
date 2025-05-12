"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""
def check_none(tuple):
    """
    :param tuple: tuple to check
    :return: True if any None value is present in the tuple, False otherwise
    """
    for i in tuple:
        if i is None:
            return True
    return False