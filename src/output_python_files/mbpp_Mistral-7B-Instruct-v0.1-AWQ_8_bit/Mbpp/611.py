"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""

def max_of_nth(matrix, n):
    """
    Returns the max of the n'th column of the matrix.
    """
    if not matrix:
        return None
    if n < 0:
        return None
    if n == 0:
        return max(matrix[0])
    else:
        return max(matrix[n])


# assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
# assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 1) == 9
# assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 0) == 5