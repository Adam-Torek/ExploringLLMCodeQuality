"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""


def sort_matrix(matrix):
    """
    Sort a given matrix in ascending order according to the sum of its rows.
    :param matrix: a matrix
    :return: a sorted matrix
    """
    matrix = sorted(matrix, key=lambda x: sum(x))
    return matrix


if __name__ == '__main__':
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1