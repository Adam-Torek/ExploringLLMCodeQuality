"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
def common_in_nested_lists(nested_lists):
    # Find the set of all elements in all nested lists
    all_elements = set()
    for list in nested_lists:
        all_elements.update(list)

    # Find the set of common elements
    common_elements = set()
    for element in all_elements:
        if nested_lists.count(element) > 0: # if the element appears more than once in nested_lists
            common_elements.add(element)

    return common_elements

# Test the function
nested_lists = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
assert set(common_in_nested_lists(nested_lists))==set([18, 12])</s>