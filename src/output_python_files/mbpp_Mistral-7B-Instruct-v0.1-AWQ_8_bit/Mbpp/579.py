"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""

def find_dissimilar(tuple1, tuple2):
    """
    This function takes two tuples as input and returns the dissimilar elements in them.
    """
    dissimilar = []
    for i in tuple1:
        if i not in tuple2:
            dissimilar.append(i)
    for i in tuple2:
        if i not in tuple1:
            dissimilar.append(i)
    return dissimilar

# Test the function
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)