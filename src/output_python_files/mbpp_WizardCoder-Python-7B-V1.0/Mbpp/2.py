"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""

def similar_elements(list1, list2):
    return set(list1) & set(list2)

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)) == set((4, 5))