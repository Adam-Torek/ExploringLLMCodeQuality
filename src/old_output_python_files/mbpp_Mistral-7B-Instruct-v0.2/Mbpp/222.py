"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""
def check_type(tuple_):
    """
    :param tuple_: tuple
    :return: bool
    """
    data_type = type(tuple_[0])
    for i in tuple_:
        if type(i) != data_type:
            return False
    return True

assert check_type((5, 6, 7, 3, 5, 6)) == True
assert check_type((5, 6, 7, 3, 5, "six")) == False
assert check_type((5, 6, 7, 3, 5, 6.0)) == True
assert check_type((5, 6, 7, 3, 5, [1, 2, 3])) == False