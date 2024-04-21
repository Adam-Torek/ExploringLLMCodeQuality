"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
def magic_square_test(matrix):
    # Check if the matrix is a square
    if len(matrix)!= len(matrix[0]):
        return False

    # Check if the matrix contains only integers
    for row in matrix:
        for num in row:
            if not isinstance(num, int):
                return False

    # Check if the matrix is a magic square
    for i in range(len(matrix)):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j] for j in range(len(matrix)))
        diag_sum = sum(matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix)))
        if row_sum!= col_sum!= diag_sum:
            return False

    return True

# Test the function
print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])) # True
print(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # False
print(magic_square_test([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])) # True<|endoftext|>