"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""

def find_dissimilar(tuple1, tuple2):
    """
    This function takes two tuples as input and returns the dissimilar elements in them.
    """
    # converting both the tuples to sets
    set1 = set(tuple1)
    set2 = set(tuple2)

    # finding the dissimilar elements using set difference
    dissimilar = set1.difference(set2)

    # converting the set of dissimilar elements back to a list and returning it
    return list(dissimilar)

# testing the function
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)