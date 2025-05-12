"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""


def frequency_lists(lists):
    """
    :param lists: list of lists
    :return: dictionary of frequency of each element in a flattened list of lists
    """
    # your code here
    return {x: lists.count(x) for x in lists}


if __name__ == '__main__':
    print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))
    print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))
    print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))
    print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))
    print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))
    print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5], [1,