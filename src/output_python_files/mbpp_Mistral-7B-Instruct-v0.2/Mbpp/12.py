"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""
def sort_matrix(matrix):
    # sort rows based on sum of elements in each row
    matrix.sort(key=lambda row: sum(row))
    return matrix

# test case
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
assert sort_matrix(matrix) == [[1, 1, 1], [1, 2, 3], [2, 4, 5]]</s>