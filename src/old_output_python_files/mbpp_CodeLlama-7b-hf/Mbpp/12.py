"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""


def sort_matrix(matrix):
    """
    Sort a given matrix in ascending order according to the sum of its rows.
    :param matrix: a list of lists
    :return: a list of lists
    """
    matrix_sum = []
    for row in matrix:
        matrix_sum.append(sum(row))
    matrix_sum.sort()
    sorted_matrix = []
    for i in range(len(matrix_sum)):
        for row in matrix:
            if sum(row) == matrix_sum[i]:
                sorted_matrix.append(row)
    return sorted_matrix


if __name__ == '__main__':
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1,