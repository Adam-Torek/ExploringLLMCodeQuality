"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""


def magic_square_test(matrix):
    """
    :param matrix: a matrix
    :return: True if the matrix is a magic square, False otherwise
    """
    # Your code here
    if len(matrix) != len(matrix[0]):
        return False
    if len(matrix) % 2 == 0:
        return False
    if len(matrix) == 1:
        return True
    if len(matrix) == 2:
        return matrix[0][0] == matrix[1][1] and matrix[0][1] == matrix[1][0]
    if len(matrix) == 3:
        return matrix[0][0] == matrix[1][1] and matrix[0][1] == matrix[1][0] and matrix[0][2] == matrix[1][2] and matrix[1][0] == matrix[2][1] and matrix[1][1] == matrix[2][0] and matrix[1][2] == matrix[2][1] and matrix[2][0] == matrix[0][2] and matrix[2][1] == matrix[0][1] and matrix[2][2] == matrix[0][0]
    if len(matrix) == 4:
        return matrix[0][0] == matrix[1][1] and matrix[0][1] == matrix[1][0] and matrix[0][2] == matrix[1][3] and matrix[0][3] == matrix[1][2] and matrix[1][0] == matrix[2][1] and matrix[1][1] == matrix[2][0] and matrix[1][2] == matrix[2][3] and matrix[1][3] == matrix[2][2] and matrix[2][0] == matrix[3][1] and matrix[2][1] == matrix[3][0] and matrix[2][2] == matrix[3][3] and matrix[2][3] == matrix[3][2] and matrix[3][0] == matrix[0][3] and matrix[3][1] == matrix[0][2] and matrix[3][2] == matrix[0][1] and matrix[3][3] == matrix[0][0]
    if len(matrix) == 5:
        return matrix[0][0] == matrix[1][1] and matrix[0][1] == matrix[1][0] and matrix[0][2] == matrix[1][3] and matrix[0][3] == matrix[1][2] and matrix[0][4] == matrix[1][4] and matrix[1][0] == matrix[2][1] and matrix[1][1] == matrix[2][0] and matrix[1][2] == matrix[2][3] and matrix[1][3] == matrix[2][2] and matrix[1][4] == matrix[2][4] and matrix[2][0] == matrix[3][1] and matrix[2][1] == matrix[3][0] and matrix[2][2] == matrix[3][3] and matrix[2][3] == matrix[3][2] and matrix[2][4] == matrix[3][4] and matrix[3][0] == matrix[4][1] and matrix[3][1] == matrix[4][0] and matrix[3][2] == matrix[4][3] and matrix[3][3] == matrix[4][2] and matrix[3][4] == matrix[4][4] and matrix[4][0] == matrix[0][4] and matrix[4][1] == matrix[0][3] and matrix[4][2] == matrix[0][2] and matrix[4][3] == matrix[0][1] and matrix[4][4] == matrix[0][0]
    if len(matrix) == 6:
        return matrix[0][0] == matrix[1][1] and matrix[0][1] == matrix[1][0] and matrix[0][2] == matrix[1][3] and matrix[0][