"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""
def check_none(tuple):
    """
    :param tuple: tuple to check for None values
    :return: boolean value indicating if there is any None value in the tuple
    """
    for i in tuple:
        if i is None:
            return True
    return False