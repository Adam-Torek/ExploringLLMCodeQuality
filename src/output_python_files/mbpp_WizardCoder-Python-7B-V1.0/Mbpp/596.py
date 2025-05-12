"""
Write a function to find the size in bytes of the given tuple.
assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
"""

import sys

def tuple_size(tup):
    return sys.getsizeof(tup)

# Test the function with an example tuple
print(tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))