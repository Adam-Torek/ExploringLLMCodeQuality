"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""


def sort_matrix(matrix):
    """
    :param matrix: list of lists
    :return: list of lists
    """
    matrix.sort(key=lambda x: sum(x))
    return matrix


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
    print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                       [1, 1, 1], [1,