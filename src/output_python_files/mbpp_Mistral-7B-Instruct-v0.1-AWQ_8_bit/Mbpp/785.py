"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(tuple_str):
    """
    Convert tuple string to integer tuple.
    """
    tuple_list = tuple_str.split(",")
    tuple_list = [int(x) for x in tuple_list]
    return tuple(tuple_list)


# assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
# assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)