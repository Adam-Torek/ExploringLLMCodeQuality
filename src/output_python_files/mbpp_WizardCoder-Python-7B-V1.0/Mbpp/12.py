"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""

def sort_matrix(matrix):
    return sorted(matrix, key=lambda row: sum(row))

# Test cases
print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])) # should return [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
print(sort_matrix([[4, 3, 2], [1, 2, 3], [5, 6, 7]])) # should return [[1, 2, 3], [4, 3, 2], [5, 6, 7]]
print(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # should return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sort_matrix([[1, 3, 5], [2, 2, 4], [3, 1, 6]])) # should return [[1, 3, 5], [2, 2, 4], [3, 1, 6]]
print(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])) # should return [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])) # should return [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
print(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])) # should return [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
print(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]])) # should return [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
print(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]])) # should return [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 1