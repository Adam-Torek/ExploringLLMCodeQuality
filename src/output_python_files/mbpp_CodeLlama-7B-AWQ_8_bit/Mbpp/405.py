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
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'x'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'e'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'o'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'u'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'c'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'a'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 't'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'y'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'z'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'f'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'g'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'h'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'i'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'j'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'k'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'l'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'm'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'n'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'p'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'q'))
    print(check_tuplex(("w", 3, "r", "e", "s", "o", "u