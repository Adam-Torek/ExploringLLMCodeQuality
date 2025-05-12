"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""
def sort_matrix(matrix):
    matrix.sort(key=lambda x: sum(x), reverse=True)
    return matrix

# test
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
assert sort_matrix(matrix) == [[1, 1, 1], [1, 2, 3], [2, 4, 5]]