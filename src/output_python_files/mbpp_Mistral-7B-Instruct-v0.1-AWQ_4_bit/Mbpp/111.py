"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""

def common_in_nested_lists(lst):
    """
    :param lst: nested list
    :return: set of common elements
    """
    common = set()
    for sublist in lst:
        for item in sublist:
            if item in common:
                common.add(item)
            else:
                common.add(item)
    return common


if __name__ == '__main__':
    assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])