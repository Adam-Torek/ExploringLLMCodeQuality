"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""

def magic_square_test(matrix):
    n = len(matrix)
    total = (n * (n + 1)) // 2
    for row in matrix:
        sum_row = sum(row)
        if sum_row != total:
            return False
        for col in range(n):
            if row[col] + row[-col - 1] != total:
                return False
    return True