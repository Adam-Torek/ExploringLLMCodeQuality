"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""

def similar_elements(list1, list2):
    """
    :param list1: first list
    :param list2: second list
    :return: set of shared elements
    """
    # create a set of first list
    set1 = set(list1)
    # create a set of second list
    set2 = set(list2)
    # find intersection of two sets
    intersection = set1 & set2
    # return intersection
    return intersection

# test the function
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))