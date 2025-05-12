"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""
def check_smaller(tuple1, tuple2):
    """
    :param tuple1: first tuple
    :param tuple2: second tuple
    :return: boolean value
    """
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must have the same length")

    for i in range(len(tuple1)):
        if tuple1[i] > tuple2[i]:
            return False

    return True

assert check_smaller((1, 2, 3), (2, 3, 4)) == False
assert check_smaller((1, 2, 3), (1, 2, 4)) == False
assert check_smaller((1, 2, 3), (1, 2, 3)) == True