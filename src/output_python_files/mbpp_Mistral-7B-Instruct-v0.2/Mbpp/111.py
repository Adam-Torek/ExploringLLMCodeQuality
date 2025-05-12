"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
def common_in_nested_lists(nested_lists):
    if not nested_lists:
        return set()

    first_list = nested_lists[0]
    common_elements = set(first_list)

    for list_ in nested_lists[1:]:
        common_elements &= set(list_)

    return common_elements

# Test the function
nested_lists = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
assert set(common_in_nested_lists(nested_lists)) == set([18, 12])