"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""

def add_lists(lst, tup):
    return tup + tuple(lst)

# Test cases
print(add_lists([5, 6, 7], (9, 10))) # Output: (9, 10, 5, 6, 7)
print(add_lists([1, 2, 3], (4, 5))) # Output: (4, 5, 1, 2, 3)
print(add_lists([], (1, 2, 3))) # Output: (1, 2, 3)
print(add_lists([], ())) # Output: ()
print(add_lists([1], (2, 3, 4, 5))) # Output: (2, 3, 4, 5, 1)
print(add_lists([1, 2, 3, 4, 5], ())) # Output: (1, 2, 3, 4, 5)
print(add_lists([], (1, 2, 3, 4, 5))) # Output: (1, 2, 3, 4, 5)
print(add_lists([1, 2, 3, 4, 5], (1, 2, 3, 4, 5))) # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Add your own test cases here