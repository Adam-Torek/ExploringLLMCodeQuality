"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
def is_magic_square(matrix):
    n = len(matrix)
    sum_row = sum(matrix[i][:])
    sum_col = [sum(row[i] for row in matrix) for i in range(n)]
    return all(sum_row == sum_col) and sum_row == (n * (n**2 + n + 1) // 2)

assert is_magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True
assert is_magic_square([[1, 2, 3, 4], [8, 1, 6, 3], [3, 5, 7, 9], [4, 9, 2, 1]]) == True
assert is_magic_square([[1, 2, 3, 4], [8, 1, 6, 3], [3, 5, 7, 9], [4, 9, 2, 1]]) == False