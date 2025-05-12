"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""

def magic_square_test(matrix):
    n = len(matrix)
    magic_sum = 0
    for i in range(n):
        for j in range(n):
            magic_sum += matrix[i][j]
    if magic_sum % n != 0:
        return False
    magic_sum = magic_sum // n
    for i in range(n):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(n))
        if row_sum != magic_sum or col_sum != magic_sum:
            return False
    diagonal_sum = sum(matrix[i][i] for i in range(n))
    diagonal_sum2 = sum(matrix[i][n-i-1] for i in range(n))
    if diagonal_sum != diagonal_sum2:
        return False
    return True

# Test
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True
assert magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == False
assert magic_square_test([[4, 9, 2], [3, 5, 7], [6, 8, 1]]) == True
assert magic_square_test([[1, 2, 3, 4, 5], [2, 5, 1, 6], [3, 1, 2, 7], [4, 6, 5, 8]]) == False
assert magic_square_test([[1, 2, 3, 4], [2, 5, 1, 6], [3, 1, 2, 7], [4, 6, 5, 8]]) == True
assert magic_square_test([[1, 2, 3], [2, 5, 6], [3, 1, 7], [4, 6, 8]]) == False
assert magic_square_test([[1, 2, 3, 4], [2, 5, 1, 6], [3, 1, 2, 7], [4, 6, 5, 8]]) == False
assert magic_square_test([[1, 2, 3, 4], [2, 5, 1, 6], [3, 1, 2, 7], [4, 6, 5, 8]]) == False
assert magic_square_test([[1, 2, 3, 4], [2, 5, 1, 6], [3, 1, 2, 7], [4, 6, 5, 8]]) == False
assert magic_square_test([[1, 2, 3, 4], [2, 5, 1, 6], [3, 1, 2, 7], [4, 6, 5, 8]]) == False
assert magic_square_test([[1, 2, 3, 4], [2, 5, 1, 6], [3, 1, 2, 7], [4, 6, 5, 8]]) == False
assert magic_square_test([[1, 2, 3, 4], [2, 5, 1, 6], [3, 1, 2, 7], [4, 6, 5, 8]]) == False
assert magic_square_test([[1, 2, 3, 4], [2, 5, 1, 6], [3, 1, 2, 7], [4, 6, 5, 8]]) == False
assert magic_square_test([[1