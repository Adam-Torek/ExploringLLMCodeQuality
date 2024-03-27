def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

#     # Using set to remove duplicates
#     return sorted(list(set(l)))

#     # Using a dictionary to keep track of unique elements
#     unique_dict = {}
#     for elem in l:
#         if elem not in unique_dict:
#             unique_dict[elem] = True
#     return sorted(unique_dict.keys())

    # Using a set to keep track of unique elements
    unique_set = set()
    for elem in l:
        if elem not in unique_set:
            unique_set.add(elem)
    return sorted(unique_set)

# Test cases
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
print(unique([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(unique([1, 2, 3, 4, 5, 5]))  # Output: [1, 2, 3, 4, 5]
print(unique([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]<|endoftext|>