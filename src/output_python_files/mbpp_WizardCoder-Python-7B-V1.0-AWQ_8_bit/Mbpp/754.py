"""
We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
"""

def extract_index_list(l1, l2, l3):
    common_elements = []
    for i in range(len(l1)):
        if l1[i] == l2[i] == l3[i]:
            common_elements.append(l1[i])
    return common_elements

# Testing the function
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7] ) == [1, 7]
assert extract_index_list([1, 2, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7] ) == []
assert extract_index_list([1, 2, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 8] ) == [1]
assert extract_index_list([1, 2, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 6] ) == [1, 7]
assert extract_index_list([1, 2, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 6] ) == [1, 7]
assert extract_index_list([1, 2, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 6] ) == [1, 7]
assert extract_index_list([1, 2, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 6] ) == [1, 7]
assert extract_index_list([1, 2, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 6] ) == [1, 7]
assert extract_index_list([1, 2, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 6] ) == [1, 7]
assert extract_index_list([1, 2, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 6] ) == [1, 7]
assert extract_index_list([1, 2, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4