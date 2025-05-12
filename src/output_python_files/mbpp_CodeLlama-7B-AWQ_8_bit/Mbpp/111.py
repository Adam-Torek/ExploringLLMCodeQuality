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
            for k in nested_list[i]:
                if k in nested_list[j]:
                    if k not in common_elements:
                        common_elements.append(k)
    return common_elements


if __name__ == '__main__':
    print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))
    print(common_in_nested_lists([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]))
    print(common_in_nested_lists([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]))
    print(common_in_nested_lists([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
                                  [1, 2, 3, 4, 5]]))
    print(common_in_nested_lists([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
                                  [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]))
    print(common_in_nested_lists([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
                                  [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]))
    print(common_in_nested_lists([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
                                  [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]))
    print(common_in_nested_lists([[1, 2,