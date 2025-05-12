"""
Write a function which given a matrix represented as a list of lists returns the max of then'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""

def max_of_nth(matrix, n):
    return max(row[n-1] for row in matrix)

# Test cases
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19<|endoftext|>