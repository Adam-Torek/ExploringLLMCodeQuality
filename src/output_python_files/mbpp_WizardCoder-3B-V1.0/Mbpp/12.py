"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""

def sort_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols-1):
            if matrix[i][j] + matrix[i][j+1] < matrix[i][j]:
                matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
    return matrix

# Test the function
print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))<|endoftext|>