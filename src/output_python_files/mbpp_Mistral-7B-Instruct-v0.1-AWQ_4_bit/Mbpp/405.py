"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""

def check_tuplex(tuple_list, element):
    """
    This function checks whether an element exists in a tuple.
    :param tuple_list: A tuple
    :param element: The element to be checked
    :return: True if the element exists in the tuple, False otherwise
    """
    for item in tuple_list:
        if item == element:
            return True
    return False