"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""

def common_in_nested_lists(lists):
    common = set(lists[0])
    for i in range(1, len(lists)):
        common.intersection_update(lists[i])
    return common

# Testing the function
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]) == set([18, 12])

# Testing the function with another example
assert set(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 5, 6], [3, 7, 8, 9], [1, 3, 10, 11]]) == set([3])

# Testing the function with another example
assert set(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 5, 6], [3, 7, 8, 9], [1, 3, 10, 11], [4, 5, 6, 7]]) == set([])

# Testing the function with another example
assert set(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 5, 6], [3, 7, 8, 9], [1, 3, 10, 11], [4, 5, 6, 7], [1, 2, 3]]) == set([3])

# Testing the function with another example
assert set(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 5, 6], [3, 7, 8, 9], [1, 3, 10, 11], [4, 5, 6, 7], [1, 2, 3], [1, 2, 3]]) == set([3])

# Testing the function with another example
assert set(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 5, 6], [3, 7, 8, 9], [1, 3, 10, 11], [4, 5, 6, 7], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) == set([3])

# Testing the function with another example
assert set(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 5, 6], [3, 7, 8, 9], [1, 3, 10, 11], [4, 5, 6, 7], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) == set([3])

# Testing the function with another example
assert set(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 5, 6], [3, 7, 8, 9], [1, 3, 10, 11], [4, 5, 6, 7], [1, 2, 3], [1,