"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
def is_magic_square(matrix):
    n = len(matrix)
    if len(matrix) != len(matrix[0]):
        return False

    sum_row = sum(matrix[i][:] for i in range(n))
    sum_col = [sum(row[i] for row in matrix) for i in range(n)]
    return all(sum_row) == sum_col and all(sum_row[i] == sum_col[i] for i in range(n))

def magic_square_test(matrix):
    assert is_magic_square(matrix) == True

matrix = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
magic_square_test(matrix)