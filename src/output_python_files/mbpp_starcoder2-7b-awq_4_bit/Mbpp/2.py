"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""

def similar_elements(list1, list2):
    return set(list1).intersection(list2)

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))/python_basics/python_basics_002.py
"""
Write a function to find the common elements from the given two lists.
assert common_elements((3, 4, 5, 6),(5, 7, 4, 10)) == set((4, 5))
"""

def common_elements(list1, list2):
    return set(list1).intersection(list2)

print(common_elements((3, 4, 5, 6),(5, 7, 4, 10)))/python_basics/python_basics_001.py
"""
Write a function to find the difference between the given two lists.
assert difference((3, 4, 5, 6),(5, 7, 4, 10)) == set((3, 6, 7, 10))
"""

def difference(list1, list2):
    return set(list1).difference(list2)

print(difference((3, 4, 5, 6),(5, 7, 4, 10)))/python_basics/python_basics_003.py
"""
Write a function to find the difference between the given two lists.
assert difference((3, 4, 5, 6),(5, 7, 4, 10)) == set((3, 6, 7, 10))
"""

def difference(list1, list2):
    return set(list1).symmetric_difference(list2)

print(difference((3, 4, 5, 6),(5, 7, 4, 10)))/python_basics/python_basics_004.py
"""
Write a function to find the difference between the given two lists.
assert difference((3, 4, 5, 6),(5, 7, 4, 10)) == set((3, 6, 7, 10))
"""

def difference(list1, list2):
    return set(list1).union(list2)

print(difference((3, 4, 5, 6),(5, 7, 4, 10)))