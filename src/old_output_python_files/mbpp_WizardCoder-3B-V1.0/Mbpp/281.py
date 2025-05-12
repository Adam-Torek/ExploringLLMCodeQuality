"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""

def all_unique(lst):
    return len(lst) == len(set(lst))

# Test cases
print(all_unique([1,2,3])) # True
print(all_unique([1,2,2])) # False
print(all_unique([1,2,3,4])) # False<|endoftext|>