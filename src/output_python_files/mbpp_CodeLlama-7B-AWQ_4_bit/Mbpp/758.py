"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""


def unique_sublists(lst):
    """
    :param lst: list of lists
    :return: dictionary of unique sublists and their occurencies
    """
    return {tuple(sorted(sublist)): lst.count(sublist) for sublist in lst}


if __name__ == '__main__':
    print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
    print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
    print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
    print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1, 3], [13, 15, 17], [5, 7], [9, 11], [1,