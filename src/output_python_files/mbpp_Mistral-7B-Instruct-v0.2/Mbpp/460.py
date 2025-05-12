"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""
def Extract(input_list):
    """
    This function takes a list as an argument and returns a new list containing the first elements of each sublist.

    :param input_list: list
    :return: list
    """
    return [sublist[0] for sublist in input_list]

# Test the function
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]