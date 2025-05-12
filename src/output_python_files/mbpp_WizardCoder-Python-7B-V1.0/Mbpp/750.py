"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""

def add_tuple(lst, tup):
    lst.extend(tup)
    return lst

# Test cases
print(add_tuple([5, 6, 7], (9, 10))) # Output: [5, 6, 7, 9, 10]
print(add_tuple([], (1, 2, 3, 4))) # Output: [1, 2, 3, 4]
print(add_tuple([], ())) # Output: []
print(add_tuple([1], (2,))) # Output: [1, 2]
print(add_tuple([1, 2, 3], (4, 5, 6, 7))) # Output: [1, 2, 3, 4, 5, 6, 7]
print(add_tuple([], ())) # Output: []
print(add_tuple([1, 2, 3], ())) # Output: [1, 2, 3]
print(add_tuple([], (1, 2, 3))) # Output: [1, 2, 3]
print(add_tuple([1, 2, 3], (4))) # Output: [1, 2, 3, 4]
print(add_tuple([1, 2, 3], ())) # Output: [1, 2, 3]
print(add_tuple([], (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add_tuple([1, 2, 3], (4, 5, 6, 7, 8, 9, 10))) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add_tuple([1, 2, 3], ())) # Output: [1, 2, 3]
print(add_tuple([], (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add_tuple([1, 2, 3], (4, 5, 6, 7, 8, 9, 10))) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add_tuple([1, 2, 3], ())) # Output: [1, 2, 3]
print(add_tuple([], (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add_tuple([1, 2, 3], (4, 5, 6, 7, 8, 9, 10))) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add_tuple([1, 2, 3], ())) # Output: [1, 2, 3]
print(add_tuple([], (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))) # Output: [1, 2, 3,