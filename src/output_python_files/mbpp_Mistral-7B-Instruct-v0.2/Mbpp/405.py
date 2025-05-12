"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""
def check_tuple(tuple_value, element):
    """
    Function to check whether an element exists within a tuple.

    :param tuple_value: tuple
    :param element: element to be checked
    :return: boolean value
    """
    if element in tuple_value:
        return True
    else:
        return False

# Testing the function
assert check_tuple(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
assert check_tuple(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'z')==False