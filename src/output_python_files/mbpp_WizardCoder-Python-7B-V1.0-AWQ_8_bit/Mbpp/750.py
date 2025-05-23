"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""

def add_tuple(lst, tup):
    lst.extend(tup)
    return lst

# Test the function with the given example
print(add_tuple([5, 6, 7], (9, 10))) # Output: [5, 6, 7, 9, 10]