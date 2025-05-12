"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""

def check_none(tuple_list):
    """
    This function checks if the given tuple has any none value or not.
    """
    for i in tuple_list:
        if i is None:
            return True
    return False


assert check_none((10, 4, 5, 6, None)) == True
assert check_none((10, 4, 5, 6)) == False