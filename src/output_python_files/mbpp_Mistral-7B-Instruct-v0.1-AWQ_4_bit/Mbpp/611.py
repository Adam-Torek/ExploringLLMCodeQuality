"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""

def max_of_nth(matrix, n):
    """
    Returns the max of the n'th column of the matrix.
    """
    if len(matrix) == 0:
        return None
    if len(matrix[0]) == 0:
        return None
    if n < 0 or n > len(matrix[0]):
        return None
    return max(matrix[i][n] for i in range(len(matrix)))