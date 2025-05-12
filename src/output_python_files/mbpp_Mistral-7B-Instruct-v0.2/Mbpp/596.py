"""
Write a function to find the size in bytes of the given tuple.
assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
"""
from sys import getsizeof

def tuple_size(t):
    return getsizeof(t)

assert tuple_size(("A", 1, "B", 2, "C", 3)) == getsizeof(("A", 1, "B", 2, "C", 3))

# Alternative solution using sum and sys.getsizeof()
def tuple_size(t):
    return sum(map(lambda x: getsizeof(x), t))

assert tuple_size(("A", 1, "B", 2, "C", 3)) == getsizeof(("A", 1, "B", 2, "C", 3))