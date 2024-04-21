"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""

def common_in_nested_lists(nested_lists):
    common_elements = []
    for i in range(len(nested_lists)):
        for j in range(len(nested_lists[i])):
            if j == 0:
                common_elements.append(nested_lists[i][j])
            else:
                if nested_lists[i][j] in common_elements:
                    common_elements.remove(nested_lists[i][j])
    return common_elements

print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))<|endoftext|>