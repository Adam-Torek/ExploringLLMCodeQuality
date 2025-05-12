"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(tuple_str):
    """
    :param tuple_str: string representation of tuple
    :return: tuple of integers
    """
    return tuple(map(int, tuple_str[1:-1].split(',')))

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
assert tuple_str_int("(1, 2, 3, 4)") == (1, 2, 3, 4)
assert tuple_str_int("(1)") == (1,)
assert tuple_str_int("()") == ()
assert tuple_str_int("(1,)") == (1,)
assert tuple_str_int("(1, 2)") == (1, 2)
assert tuple_str_int("(1, 2,)") == (1, 2)
assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
assert tuple_str_int("(1, 2, 3,)") == (1, 2, 3)
assert tuple_str_int("(1, 2, 3, 4,)") == (1, 2, 3, 4)
assert tuple_str_int("(1, 2, 3, 4, 5)") == (1, 2, 3, 4, 5)
assert tuple_str_int("(1, 2, 3, 4, 5,)") == (1, 2, 3, 4, 5)
assert tuple_str_int("(1, 2, 3, 4, 5, 6)") == (1, 2, 3, 4, 5, 6)
assert tuple_str_int("(1, 2, 3, 4, 5, 6,)") == (1, 2, 3, 4, 5, 6)
assert tuple_str_int("(1, 2, 3, 4, 5, 6, 7)") == (1, 2, 3, 4, 5, 6, 7)
assert tuple_str_int("(1, 2, 3, 4, 5, 6, 7,)") == (1, 2, 3, 4, 5, 6, 7)
assert tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8)") == (1, 2, 3, 4, 5, 6, 7, 8)
assert tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8,)") == (1, 2, 3, 4, 5, 6, 7, 8)
assert tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9)") == (1, 2, 3, 4, 5, 6, 7, 8, 9)
assert tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9,)") == (1, 2, 3, 4, 5, 6, 7, 8, 9)
assert tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)") == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
assert tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,)") == (1, 2, 3, 4, 5, 6, 7, 8, 9,