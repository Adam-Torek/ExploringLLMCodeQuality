"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""

def check_smaller(tuple1, tuple2):
    """
    This function checks if each element of second tuple is smaller than its corresponding element in the first tuple.
    """
    for i in range(len(tuple1)):
        if tuple1[i] > tuple2[i]:
            return True
    return False

assert check_smaller((1, 2, 3), (2, 3, 4)) == False