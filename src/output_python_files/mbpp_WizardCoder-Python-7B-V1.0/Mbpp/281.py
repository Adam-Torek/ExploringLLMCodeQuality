"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""

def all_unique(lst):
    return len(lst) == len(set(lst))

# Test cases
print(all_unique([1,2,3])) # True
print(all_unique([1,2,3,3])) # False
print(all_unique([1,2,3,4])) # True
print(all_unique([1,2,2,3])) # False
print(all_unique([1,2,3,4,5])) # True
print(all_unique([1,2,3,4,5,5])) # False
print(all_unique([1,2,3,4,5,6])) # True
print(all_unique([1,2,3,4,5,6,6])) # False
print(all_unique([1,2,3,4,5,6,7])) # True
print(all_unique([1,2,3,4,5,6,7,7])) # False
print(all_unique([1,2,3,4,5,6,7,8])) # True
print(all_unique([1,2,3,4,5,6,7,8,8])) # False
print(all_unique([1,2,3,4,5,6,7,8,9])) # True
print(all_unique([1,2,3,4,5,6,7,8,9,9])) # False
print(all_unique([1,2,3,4,5,6,7,8,9,10])) # True
print(all_unique([1,2,3,4,5,6,7,8,9,10,10])) # False
print(all_unique([1,2,3,4,5,6,7,8,9,10,11])) # True
print(all_unique([1,2,3,4,5,6,7,8,9,10,11,11])) # False
print(all_unique([1,2,3,4,5,6,7,8,9,10,11,12])) # True
print(all_unique([1,2,3,4,5,6,7,8,9,10,11,12,12])) # False
print(all_unique([1,2,3,4,5,6,7,8,9,10,11,12,13])) # True
print(all_unique([1,2,3,4,5,6,7,8,9,10,11,12,13,13])) # False
print(all_unique([1,2,3,4,5,6,7,8,9,10,11,12,13,14])) # True
print(all_unique([1,2,3,4,5,6,7,8,9,10,11,12,13,14,14])) # False
print(all_unique([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])) # True
print(all_unique([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15])) # False
print(all_unique([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])) # True
print(all_unique([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16])) # False
print(all_unique([1,2,3,4,5,6,7,8,9,1