"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""


def check_type(tup):
    """
    Check if all the elements in tuple have same data type or not.
    :param tup: tuple
    :return: bool
    """
    return all(isinstance(x, type(tup[0])) for x in tup)


if __name__ == '__main__':
    print(check_type((5, 6, 7, 3, 5, 6)))
    print(check_type((5, 6, 7, 3, 5, 6, 7)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11, 12)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)))
    print(check_type((5, 6, 7, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14