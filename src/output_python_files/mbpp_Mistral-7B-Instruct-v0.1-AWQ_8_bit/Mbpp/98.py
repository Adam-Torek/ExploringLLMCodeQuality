"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""

def multiply_num(lst):
    """
    multiply all the numbers in a list and divide with the length of the list
    :param lst: list of numbers
    :return: float
    """
    result = 1
    for num in lst:
        result *= num
    return result / len(lst)


# test
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)