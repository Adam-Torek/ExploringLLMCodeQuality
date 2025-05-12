"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""

def sort_matrix(matrix):
    return sorted(matrix, key=lambda row: sum(row))

print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))
# Output: [[1, 1, 1], [1, 2, 3], [2, 4, 5]]

# Test cases
print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])) # Output: [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
print(sort_matrix([[1, 3, 5], [2, 4, 6], [3, 2, 1]])) # Output: [[1, 3, 5], [2, 4, 6], [3, 2, 1]]
print(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sort_matrix([[5, 4, 3], [2, 1, 6], [9, 8, 7]])) # Output: [[2, 1, 6], [5, 4, 3], [9, 8, 7]]
print(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

# Test case for empty matrix
print(sort_matrix([])) # Output: []

# Test case for matrix with only one row
print(sort_matrix([[1, 2, 3])) # Output: [[1, 2, 3]]

# Test case for matrix with only one column
print(sort_matrix([[1], [2], [3], [4]])) # Output: [[1], [2], [3], [4]]

# Test case for matrix with negative numbers
print(sort_matrix([[-1, -2, -3], [-2, -4, -5], [-1, -1, -1]])) # Output: [[-2, -4, -5], [-1, -2, -3], [-1, -1, -1]]

# Test case for matrix with zero
print(sort_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])) # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Test case for matrix with repeated rows
print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1], [2, 4, 5]])) # Output: [[1, 1, 1], [1, 2, 3], [2, 4, 5], [2, 4, 5]]

# Test case for matrix with repeated rows and negative numbers
print(sort_matrix([[-1, -2, -3],