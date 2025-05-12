"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""


def check_tuplex(tup, elem):
    """
    Checks whether an element exists within a tuple.
    """
    return elem in tup


if __name__ == '__main__':
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'a'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'u'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'c'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'o'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'w'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u