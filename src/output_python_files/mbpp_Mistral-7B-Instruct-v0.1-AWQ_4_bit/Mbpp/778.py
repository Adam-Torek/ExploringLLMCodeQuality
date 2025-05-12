"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""

def pack_consecutive_duplicates(lst):
    """
    This function packs consecutive duplicates of a given list elements into sublists.
    """
    result = []
    i = 0
    while i < len(lst):
        if lst[i] == lst[i+1]:
            result.append(lst[i])
            i += 1
        else:
            result.append(lst[i])
            i += 1
    return result

# Test the function
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]