"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""


def check_distinct(tup):
    """
    Check if given tuple contains no duplicates.
    :param tup: tuple
    :return: bool
    """
    return len(tup) == len(set(tup))


if __name__ == '__main__':
    print(check_distinct((1, 4, 5, 6, 1, 4)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6)))
    print(check_distinct((1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1, 4, 5, 6, 1)))
    print(check_distinct((1, 4, 5,