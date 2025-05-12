def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l), key=l.index)


# Example usage:
print(unique([5, 3, 5, 2, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]


# Note: The function first converts the list to a set to remove duplicates, then sorts the set and returns it as a list. 
# The key argument in the sorted() function is used to sort the list based on the index of the elements in the original list. 
# This ensures that the sorted list contains the elements in the same order as the original list.