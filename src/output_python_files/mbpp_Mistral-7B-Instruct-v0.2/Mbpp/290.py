"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""
def max_length(lst):
    max_len = 0
    max_lst = []
    for sub_lst in lst:
        if len(sub_lst) > max_len:
            max_len = len(sub_lst)
            max_lst = sub_lst
    return max_len, max_lst

assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])</s>