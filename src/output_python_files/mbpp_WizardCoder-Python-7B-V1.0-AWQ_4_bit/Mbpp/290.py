"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""

def max_length(lst):
    max_length = 0
    max_lst = []
    for sub_lst in lst:
        if len(sub_lst) > max_length:
            max_length = len(sub_lst)
            max_lst = sub_lst
    return max_length, max_lst

# Test cases
print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])) # (3, [13, 15, 17])
print(max_length([[1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17]])) # (6, [10, 11, 12, 13, 14, 15, 16, 17])
print(max_length([[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18]])) # (7, [11, 12, 13, 14, 15, 16, 17, 18])
print(max_length([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18]])) # (7, [10, 11, 12, 13, 14, 15, 16, 17, 18])
print(max_length([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) # (1, [10])