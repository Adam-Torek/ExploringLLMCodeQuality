"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""

def similar_elements(list1, list2):
    """
    This function takes two lists as input and returns the shared elements between them.
    """
    # converting both the lists into sets
    set1 = set(list1)
    set2 = set(list2)

    # finding intersection of both sets
    intersection = set1.intersection(set2)

    # converting intersection back to list and returning it
    return list(intersection)

# testing the function
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))