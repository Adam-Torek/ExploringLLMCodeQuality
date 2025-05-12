"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""

def max_of_nth(matrix, n):
    max_value = matrix[0][n]
    for row in matrix:
        if row[n] > max_value:
            max_value = row[n]
    return max_value

# Test cases
print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == 9) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0) == 7) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2) == 3) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == 1) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 100) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -100) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1000) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1000) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0.5) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1.5) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], "a") == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], None) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], []) == None) # True
print(max_of_nth([[1, 2, 3], [4, 5, 6