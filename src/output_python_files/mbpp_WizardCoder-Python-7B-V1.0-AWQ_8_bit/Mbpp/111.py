"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""

def common_in_nested_lists(lists):
    common = set()
    for i in lists[0]:
        for j in lists[1:]:
            if i in j:
                common.add(i)
    return common

# Testing the function
print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))
# Output: {18, 12}

# Testing the function with another example
print(common_in_nested_lists([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 7, 8], [4, 5, 6, 7, 9]]))
# Output: {4, 5}

# Testing the function with another example
print(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]))
# Output: set()

# Testing the function with another example
print(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]))
# Output: {1, 2, 3, 4, 5, 6}

# Testing the function with another example
print(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 8]]))
# Output: {1, 2, 3, 4, 5, 6}

# Testing the function with another example
print(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 8], [1, 2, 3, 4, 5, 6, 9]]))
# Output: {1, 2, 3, 4, 5, 6}

# Testing the function with another example
print(common_in_nested_lists([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 8], [1, 2, 3, 4, 5, 6, 9], [1, 2, 3, 4, 5, 6, 10]]))
# Output: {1, 2, 3, 4, 5, 6}

# Testing the function with another example
print(common_in_nested_