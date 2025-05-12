"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""

def max_length(lst):
    max_length = 0
    max_lst = []
    for i in lst:
        if len(i) > max_length:
            max_length = len(i)
            max_lst = i
    return max_length, max_lst

print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])) # Output: (3, [13, 15, 17])
print(max_length([[1, 2, 3], [4, 5, 6, 7], [8, 9], [10, 11, 12, 13, 14]])) # Output: (4, [10, 11, 12, 13, 14])
print(max_length([[1], [2], [3], [4], [5]])) # Output: (1, [5])
print(max_length([[1, 2], [3, 4], [5, 6, 7, 8], [9]])) # Output: (3, [5, 6, 7, 8)