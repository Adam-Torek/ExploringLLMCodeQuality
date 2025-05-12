"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""

def add_tuple(lst, tup):
    lst.extend(tup)
    return lst

# Test the function with the given example
print(add_tuple([5, 6, 7], (9, 10))) # Output: [5, 6, 7, 9, 10]

# Test the function with other examples
print(add_tuple([1, 2, 3], (4, 5))) # Output: [1, 2, 3, 4, 5]
print(add_tuple([], (1, 2, 3, 4, 5))) # Output: [1, 2, 3, 4, 5]
print(add_tuple([], ())) # Output: []
print(add_tuple([1, 2, 3], ())) # Output: [1, 2, 3]
print(add_tuple([], (1, 2, 3))) # Output: [1, 2, 3]
print(add_tuple([1, 2, 3], ())) # Output: [1, 2, 3]
print(add_tuple([], (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add_tuple([1, 2, 3], (4, 5, 6, 7, 8, 9, 10))) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]