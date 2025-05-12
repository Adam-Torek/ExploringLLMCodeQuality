"""
Write a function to convert a list to a tuple.
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
"""

def list_tuple(lst):
    return tuple(lst)

# Test cases
print(list_tuple([5, 10, 7, 4, 15, 3])) # Output: (5, 10, 7, 4, 15, 3)
print(list_tuple([1, 2, 3, 4, 5])) # Output: (1, 2, 3, 4, 5)
print(list_tuple([100, 200, 300, 400])) # Output: (100, 200, 300, 400)
print(list_tuple([])) # Output: ()
print(list_tuple([1])) # Output: (1,)
print(list_tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)