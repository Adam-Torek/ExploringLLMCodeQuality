"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""

def all_unique(lst):
    return len(lst) == len(set(lst))

assert all_unique([1,2,3]) == True
assert all_unique([1,2,3,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10]) == True
assert all_unique([1,2,3,4,5,6,7,8,9,10,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == False
assert all_unique([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1