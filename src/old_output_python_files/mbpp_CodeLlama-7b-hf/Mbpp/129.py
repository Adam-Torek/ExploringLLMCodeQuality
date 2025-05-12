"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""


def magic_square_test(matrix):
    """
    :param matrix: a matrix
    :return: True if the matrix is a magic square, False otherwise
    """
    # check if the matrix is a square
    if len(matrix) != len(matrix[0]):
        return False
    # check if the sum of the rows is equal to the sum of the columns
    for i in range(len(matrix)):
        if sum(matrix[i]) != sum(matrix[j][i] for j in range(len(matrix))):
            return False
    # check if the sum of the diagonals is equal to the sum of the rows
    if sum(matrix[i][i] for i in range(len(matrix))) != sum(matrix[i] for i in range(len(matrix))):
        return False
    return True


if __name__ == '__main__':
    print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
    print(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
    print(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]))
    print(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]))
    print(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]))
    print(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21],
                             [22, 23, 24]]))
    print(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21],
                             [22, 23, 24], [25, 26, 27]]))
    print(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21],
                             [22, 23, 24], [25, 26, 27], [28, 29, 30]]))
    print(magic