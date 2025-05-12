"""
Write a function to check if a dictionary is empty
assert my_dict({10})==False
"""
def is_empty(dictionary):
    """
    :param dictionary: a dictionary
    :return: True if the dictionary is empty, False otherwise
    """
    return len(dictionary) == 0