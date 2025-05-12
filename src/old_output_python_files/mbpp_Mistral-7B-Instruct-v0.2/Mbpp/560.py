"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""
def union_elements(tuple1, tuple2):
    """
    This function takes two tuples as arguments and returns the union of their elements in sorted order.
    """
    set1 = set(tuple1)
    set2 = set(tuple2)
    union_set = set1.union(set2)
    return list(sorted(list(union_set)))

# Test the function
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (3, 4, 5, 6, 7, 10)
assert union_elements((1, 2, 3),(3, 4, 5)) == (1, 2, 3, 4, 5)
assert union_elements((1, 2, 3),(3, 3, 3)) == (1, 2, 3)
assert union_elements((1,),(1,)) == (1)
assert union_elements((1,),()) == ()
assert union_elements((),(1,)) == (1)