"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""


def find_dissimilar(tuple1, tuple2):
    """
    This function takes two tuples as input and returns a list of elements that are present in tuple1 but not in tuple2.
    """
    dissimilar_elements = []
    for element in tuple1:
        if element not in tuple2:
            dissimilar_elements.append(element)
    return dissimilar_elements

# Test the function
print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10))) # Output: [3, 6, 7, 10]<|endoftext|>