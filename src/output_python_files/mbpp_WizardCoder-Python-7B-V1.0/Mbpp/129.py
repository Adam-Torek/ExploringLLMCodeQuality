"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
def magic_square_test(matrix):
    n = len(matrix)
    if n == 0:
        return False
    if n % 2 == 0 or n % 3 != 0:
        return False
    magic_sum = n * (n * n + 1) / 2
    row_sum = col_sum = diag_sum = 0
    for i in range(n):
        row_sum += matrix[i][i]
        col_sum += matrix[i][n-i-1]
        diag_sum += matrix[i][i]
        diag_sum += matrix[n-i-1][i]
    if row_sum != magic_sum or col_sum != magic_sum or diag_sum != magic_sum:
        return False
    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += matrix[i][j]
        if row_sum != magic_sum:
            return False
    return True

# Test cases
print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])) # True
print(magic_square_test([[4, 9, 2, 3], [3, 5, 5, 8], [6, 1, 10, 1], [8, 8, 1, 6]])) # False
print(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # False
print(magic_square_test([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])) # True
print(magic_square_test([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])) # False
print(magic_square_test([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])) # True
print(magic_square_test([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]])) # False
print(magic_square_test([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31