"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""


def common_in_nested_lists(nested_list):
    """
    :param nested_list: list of lists
    :return: list of common elements
    """
    common_elements = []
    for i in range(len(nested_list)):
        for j in range(i + 1, len(nested_list)):
            common_elements += list(set(nested_list[i]).intersection(nested_list[j]))
    return list(set(common_elements))


if __name__ == '__main__':
    print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))
    print(common_in_nested_lists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(common_in_nested_lists([[1, 2, 3], [1, 2, 3], [1, 2, 3, 4]]))
    print(common_in_nested_lists([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3]]))
    print(common_in_nested_lists([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 5]]))
    print(common_in_nested_lists([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6]]))
    print(common_in_nested_lists([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6], [1, 2, 3, 7]]))
    print(common_in_nested_lists([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6], [1, 2, 3, 7], [1, 2, 3, 8]]))
    print(common_in_nested_lists([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6], [1, 2, 3, 7], [1, 2, 3, 8],
                                  [1, 2, 3, 9]]))
    print(common_in_nested_lists([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6], [1, 2, 3, 7], [1, 2, 3, 8],
                                  [1, 2, 3, 9], [1, 2, 3, 10]]))
    print(common_in_nested_lists([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6