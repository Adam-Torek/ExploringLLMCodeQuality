"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""
def check_tuple(tuple_value, element):
    """
    :param tuple_value: tuple
    :param element: element to check
    :return: boolean value
    """
    if element in tuple_value:
        return True
    else:
        return False

assert check_tuple(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
assert check_tuple(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'z')==False</s>