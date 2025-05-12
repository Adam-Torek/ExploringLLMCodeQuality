"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""

def check_K(tuples, k):
    """
    :param tuples: list of tuples
    :param k: integer
    :return: True if k is present in tuples else False
    """
    for tuple in tuples:
        if k in tuple:
            return True
    return False


# assert check_K((10, 4, 5, 6, 8), 6) == True
# assert check_K((10, 4, 5, 6, 8), 7) == False