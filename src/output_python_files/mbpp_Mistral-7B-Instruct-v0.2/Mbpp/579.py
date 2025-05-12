"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""
def find_dissimilar(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    dissimilar = list(set1.difference(set2))
    dissimilar.extend(list(set2.difference(set1)))
    return dissimilar

assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)