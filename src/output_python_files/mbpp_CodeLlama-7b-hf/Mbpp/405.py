"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""


def check_tuplex(tup, element):
    """
    Checks whether an element exists within a tuple.
    :param tup: tuple
    :param element: element to be checked
    :return: True if element exists in tuple, False otherwise
    """
    return element in tup


if __name__ == '__main__':
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'x'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 3))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 3.0))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 3.1))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 3.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000