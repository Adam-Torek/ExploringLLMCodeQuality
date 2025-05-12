"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""

def find_dissimilar(tuple1, tuple2):
    return tuple(set(tuple1).symmetric_difference(set(tuple2)))

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))
"""
Write a function to find the common elements in the given two tuples.
assert find_common((3, 4, 5, 6), (5, 7, 4, 10)) == (4, 5)
"""

def find_common(tuple1, tuple2):
    return tuple(set(tuple1).intersection(set(tuple2)))

print(find_common((3, 4, 5, 6), (5, 7, 4, 10)))
"""
Write a function to find the common elements in the given two lists.
assert find_common([3, 4, 5, 6], [5, 7, 4, 10]) == [4, 5]
"""

def find_common(list1, list2):
    return list(set(list1).intersection(set(list2)))

print(find_common([3, 4, 5, 6], [5, 7, 4, 10]))
"""
Write a function to find the common elements in the given two sets.
assert find_common({3, 4, 5, 6}, {5, 7, 4, 10}) == {4, 5}
"""

def find_common(set1, set2):
    return set(set1).intersection(set(set2))

print(find_common({3, 4, 5, 6}, {5, 7, 4, 10}))
"""
Write a function to find the dissimilar elements in the given two sets.
assert find_dissimilar({3, 4, 5, 6}, {5, 7, 4, 10}) == {3, 6, 7, 10}
"""

def find_dissimilar(set1, set2):
    return set(set1).symmetric_difference(set(set2))

print(find_dissimilar({3, 4, 5, 6}, {5, 7, 4, 10}))
"""
Write a function to find the common elements in the given two lists.
assert find_common([3, 4, 5, 6], [5, 7, 4, 10]) == [4, 5]
"""

def find_common(list1, list2):
    return list(set(list1).intersection(set(list2)))

print(find_common([3, 4, 5, 6], [5, 7, 4, 10]))
"""
Write a function to find the common elements in the given two sets.
assert find_common({3, 4, 5, 6}, {5, 7, 4, 10}) == {4, 5}
"""

def find_common(set1, set2):
    return set(set1).intersection(set(set2))

print(find_common({3, 4, 5, 6}, {5, 7, 4, 10}))
"""
Write a function to find the dissimilar elements in the given two sets.
assert find_dissimilar({3, 4, 5, 6}, {5, 7, 4, 10}) == {3, 6, 7, 10}
"""

def find_dissimilar(set1, set2):
    return set(set1).symmetric_difference(set(set2))

print(find_dissimilar({3, 4, 5, 6}, {5, 7, 4, 10}))
"""
Write a function to find the common elements in the given two lists.
assert find_common([3, 4, 5, 6], [5, 7, 4, 10]) == [4