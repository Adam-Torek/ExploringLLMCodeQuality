"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""


def sort_matrix(matrix):
    """
    :param matrix: a matrix of integers
    :return: a matrix sorted according to the sum of its rows
    """
    matrix_sorted = []
    for i in range(len(matrix)):
        matrix_sorted.append(sorted(matrix[i], reverse=True))
    return matrix_sorted


if __name__ == '__main__':
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1