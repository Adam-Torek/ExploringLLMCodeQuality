"""
Write a function to find the size in bytes of the given tuple.
assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
"""

def tuple_size(tuple_):
    """
    Returns the size of the given tuple in bytes.
    """
    return sys.getsizeof(tuple_)