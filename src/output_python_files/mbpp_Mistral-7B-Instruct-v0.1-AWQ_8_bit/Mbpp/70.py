"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""

def get_equal(tuples):
    """
    :param tuples: list of tuples
    :return: True if all tuples have same length, False otherwise
    """
    if len(tuples) == 0:
        return True
    else:
        for i in range(len(tuples)):
            if len(tuples[i]) != len(tuples[0]):
                return False
        return True