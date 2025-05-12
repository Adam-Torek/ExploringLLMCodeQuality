"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""

def get_equal(tuples):
    """
    :param tuples: list of tuples
    :return: True if all tuples have equal length, False otherwise
    """
    if not tuples:
        return True
    else:
        return all(len(t) == len(tuples[0]) for t in tuples)