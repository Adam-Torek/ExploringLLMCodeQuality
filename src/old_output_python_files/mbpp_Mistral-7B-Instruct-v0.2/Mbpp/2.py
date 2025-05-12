"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""
def similar_elements(list1, list2):
    """
    :param list1: list of elements
    :param list2: list of elements
    :return: set of common elements
    """
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == "__main__":
    assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
    assert set(similar_elements((1, 2, 3, 4),(3, 4, 5, 6))) == set()
    assert set(similar_elements((1, 2, 3, 4),(3, 4, 3, 4))) == set((3, 4))
    assert set(similar_elements((1, 2, 3, 4),(3, 4, 3, 4, 1))) == set((3, 4))
    assert set(similar_elements((1, 2, 3, 4),(3, 4, 3, 4, 1, 2))) == set((3, 4))