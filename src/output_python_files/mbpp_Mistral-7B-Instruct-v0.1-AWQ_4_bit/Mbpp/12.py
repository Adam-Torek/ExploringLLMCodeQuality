"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""

def sort_matrix(matrix):
    """
    This function takes a matrix as input and returns a new matrix sorted in ascending order according to the sum of its rows.
    """
    matrix = sorted(matrix, key=lambda x: sum(x))
    return matrix

# test
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
assert sort_matrix(matrix)==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]