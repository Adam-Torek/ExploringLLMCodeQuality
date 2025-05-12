"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""

def max_length(lst):
    max_len = 0
    max_lst = []
    for sublist in lst:
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_lst = sublist
    return max_len, max_lst

# assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))