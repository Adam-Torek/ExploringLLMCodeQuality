"""
Write a function to check if a dictionary is empty
assert my_dict({10})==False
"""

def is_empty(dictionary):
    """
    This function checks if a dictionary is empty
    :param dictionary: input dictionary
    :return: True if dictionary is empty, False otherwise
    """
    if len(dictionary) == 0:
        return True
    else:
        return False