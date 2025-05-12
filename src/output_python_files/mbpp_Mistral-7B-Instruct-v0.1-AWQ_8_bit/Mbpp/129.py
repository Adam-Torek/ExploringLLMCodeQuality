"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""

def magic_square_test(matrix):
    n = len(matrix)
    total = (n*(n**2+1))//2
    sum = 0
    for row in matrix:
        sum += sum(row)
    return sum == total

matrix = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
print(magic_square_test(matrix))