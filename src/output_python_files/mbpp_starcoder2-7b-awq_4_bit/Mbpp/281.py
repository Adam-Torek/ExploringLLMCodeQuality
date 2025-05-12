"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""

def all_unique(lst):
    return len(lst) == len(set(lst))

assert all_unique([1,2,3]) == True
assert all_unique([1,2,3,1]) == False
assert all_unique([1,2,3,1,2]) == False
assert all_unique([1,2,3,1,2,3]) == False
assert all_unique([1,2,3,1,2,3,1]) == False
assert all_unique([1,2,3,1,2,3,1,2]) == False
assert all_unique([1,2,3,1,2,3,1,2,3]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1]) == False
assert all_unique([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2]) == False
assert all_unique([1,2,3,1,2,3,1