"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""
def get_equal(tuples):
    """
    :param tuples: list of tuples
    :return: boolean value
    """
    if len(tuples) == 0:
        return True
    return all(map(len, tuples))

assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
assert get_equal([(11, 22), (44, 55)]) == True
assert get_equal([(11, 22), (44)]) == False
assert get_equal([]) == True