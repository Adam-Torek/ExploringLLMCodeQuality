"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""

def union_elements(tup1, tup2):
    """
    This function takes two tuples as input and returns a new tuple containing the union of their elements in sorted order.
    """
    # Convert the tuples to sets to remove duplicates and then back to tuples
    set1 = set(tup1)
    set2 = set(tup2)
    union_set = set1.union(set2)
    return tuple(sorted(union_set))

# Test the function
print(union_elements((3, 4, 5, 6), (5, 7, 4, 10))) # Output: (3, 4, 5, 6, 7, 10)
print(union_elements((1, 2, 3), (4, 5, 6))) # Output: (1, 2, 3, 4, 5, 6)
print(union_elements((1, 2, 3), (3, 4, 5))) # Output: (1, 2, 3, 4, 5)
print(union_elements((), (4, 5, 6))) # Output: (4, 5, 6)
print(union_elements((1, 2, 3), ())) # Output: (1, 2, 3)
print(union_elements((), ())) # Output: ()