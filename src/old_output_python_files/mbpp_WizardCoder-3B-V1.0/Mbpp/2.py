"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""

def similar_elements(list1, list2):
    """
    Returns a set of elements that are present in both lists.
    """
    return set(list1) & set(list2)

# Test cases
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
assert set(similar_elements((1, 2, 3, 4, 5),(2, 4, 6, 8, 10))) == set((2, 4, 6))<|endoftext|>