"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""

def magic_square_test(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])
    for i in range(n):
        if sum(matrix[i]) != magic_sum:
            return False
        if sum(matrix[i][j] for i in range(n)) != magic_sum:
            return False
        if sum(matrix[j][i] for i in range(n)) != magic_sum:
            return False
    diagonal_sum = sum(matrix[i][i] for i in range(n))
    anti_diagonal_sum = sum(matrix[i][n-i-1] for i in range(n))
    if diagonal_sum != anti_diagonal_sum:
        return False
    return True

# Test
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
assert magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9]])==False
assert magic_square_test([[4, 9, 2], [3, 5, 7], [6, 8, 1]])==True
assert magic_square_test([[1, 2, 3, 4, 5], [2, 5, 1, 6], [3, 1, 2, 7], [4, 6, 5, 8]])==False
assert magic_square_test([[1, 2, 3, 4, 5], [2, 5, 1, 6], [3, 1, 2, 7], [4, 6, 5, 8], [5, 4, 3, 2]])==True