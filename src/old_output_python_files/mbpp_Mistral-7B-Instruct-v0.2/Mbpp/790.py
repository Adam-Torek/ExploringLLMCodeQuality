"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""
def even_position(lst):
    """
    This function checks if every even index of a given list contains an even number.

    :param lst: list
    :return: bool
    """
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            return False
    return True