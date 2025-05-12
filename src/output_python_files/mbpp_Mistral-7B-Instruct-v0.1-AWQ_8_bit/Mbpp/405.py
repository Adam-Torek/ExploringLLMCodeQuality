"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""

def check_tuplex(tuplex, element):
    """
    This function checks whether an element exists in a tuple.
    :param tuplex: tuple
    :param element: element
    :return: True if element exists in tuple, False otherwise
    """
    for item in tuplex:
        if item == element:
            return True
    return False