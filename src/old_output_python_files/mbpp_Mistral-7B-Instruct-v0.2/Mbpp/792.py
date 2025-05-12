"""
Write a python function to count the number of lists in a given number of lists.
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
"""
def count_list(input_list):
    """
    This function takes a list as an argument and returns the number of lists within the list.

    :param input_list: list
    :return: int
    """
    return len(input_list)

assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4