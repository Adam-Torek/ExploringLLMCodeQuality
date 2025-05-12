"""
Write a function to find the size in bytes of the given tuple.
assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
"""

def tuple_size(tuple_):
    return sys.getsizeof(tuple_)

# assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
# assert tuple_size(()) == sys.getsizeof(())
# assert tuple_size((1,)) == sys.getsizeof((1,))
# assert tuple_size((1, 2, 3)) == sys.getsizeof((1, 2, 3))
# assert tuple_size((1, 2, 3, 4, 5, 6)) == sys.getsizeof((1, 2, 3, 4, 5, 6))
# assert tuple_size((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == sys.getsizeof((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))